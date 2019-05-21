#-*- coding: utf-8 -*-
from Mydb import Mydb
import os
from pytils import translit
from datetime import datetime

class Wpdb(Mydb):
    def __init__(self, db_name = ''):
        Mydb.__init__(self, db_name)
        self.qthemplate = 'select option_value from wp_options where option_name="template"'
        self.qusers = 'select * from wp_users'
        self.db_name = db_name

    def get_template(self):
        return self.fetch(self.qthemplate)[0][0]

    def show_template(self):
        print self.fetch(self.qthemplate)[0][0]

    def get_users(self):
        return(self.fetch(self.qusers))

    def show_users(self):
        for x in self.fetch(self.qusers):
            print x[1]

    def get_user_id(self, name):
        quser_id = 'select ID from wp_users where user_login="' + name + '"'
        return self.fetch(quser_id)[0][0];

    def create_user(self, username, passwd, email):
        args_dict = { }
        args_dict["username"] = username
        args_dict["passwd"] = passwd
        args_dict["email"] = email
        self.qcreate_user = "INSERT INTO `wp_users` (ID, user_login, user_pass, user_nicename, user_email, user_url, user_registered, user_activation_key, user_status, display_name) VALUES (NULL, '%(username)s', MD5('%(passwd)s'), '%(username)s', '%(email)s', '', '2012-09-28 00:00:00', '', '0', '%(username)s');" % args_dict
        self.query(self.qcreate_user)

    def grant_user(self, username):
        id = self.get_user_id(username)
        id_str = str(id)
        qgrant = "INSERT INTO `wp_usermeta` (umeta_id, user_id, meta_key, meta_value) VALUES (NULL, '" + id_str + "', 'wp_capabilities', 'a:1:{s:13:\"administrator\";b:1;}')"
        self.query(qgrant)
        qgrant = "INSERT INTO `wp_usermeta` (umeta_id, user_id, meta_key, meta_value) VALUES (NULL, '" + id_str +"', 'wp_user_level', '10');"
        self.query(qgrant)


    def update_option(self, option_name, option_value):
        args_dict = {}
        args_dict["option_name"] = option_name
        args_dict["option_value"] = option_value
        qtest = "UPDATE `wp_options` SET option_value='%(option_value)s' where option_name='%(option_name)s'" % args_dict
        self.query(qtest)

    def install_wp(self, siteurl, blogname, blogdescription, admin_email, admin_name, admin_password):
        os.system('sudo ./install_wp.sh ' + self.db_name)
        self.update_option('siteurl', siteurl)
        self.update_option('home', siteurl)
        self.update_option('blogname', blogname)
        self.update_option('blogdescription', blogdescription)
        self.update_option('admin_email', admin_email)
        self.set_template('basic')
        self.create_user(admin_name, admin_password, admin_email)
        self.grant_user(admin_name)

    def set_blogname(self, blogname):
        self.update_option('blogname', blogname)

    def set_description(self, blogdescription):
        self.update_option('blogdescription', blogdescription)

    def set_template(self, template):
        self.update_option('template','basic')
        self.update_option('stylesheet', 'basic')
        self.update_option('current_theme','Basic')

    def create_category(self, category_name):
        category_jar = self.get_translite(category_name)
        for x in self.fetch("SELECT slug FROM `wp_terms`"):
            if x[0] == category_jar:
                print x[0]
                print category_jar
                print("Имя категории уже используется")
                return False
        wp_terms_query = "INSERT INTO `" + self.db_name +"`.`wp_terms` (`term_id`, `name`, `slug`, `term_group`) VALUES (NULL, '" + category_name.capitalize() + "', '" + category_jar + "', '0')"
        self.query(wp_terms_query)
        catid = self.fetch("select term_id from `wp_terms` order by term_id desc limit 1")[0][0]
        wp_terms_tax_query = "INSERT INTO `" + self.db_name +"`.`wp_term_taxonomy` (`term_taxonomy_id`, `term_id`, `taxonomy`, `description`, `parent`, `count`) VALUES (NULL, '" + str(catid) + "', 'category', '', '0', '1')"
        self.query(wp_terms_tax_query)

    def create_post(self, post_title, post_content):
        post_status="publish"
        post_name = self.get_translite(post_title)
        if(not self.check_post_name(post_name)):
            print("Не уничкальное имя поста")
            return False
        post_guid="http://" + self.db_name +"/" + post_name
        post_type="post"
        qpost = "INSERT INTO `" + self.db_name + "`.`wp_posts` (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) VALUES (NULL, '1', '" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "', '" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "', '" + post_content + "', '" + post_title + "', '', '" + post_status + "', 'open', 'open', '', '" + post_name + "', '', '', '2017-02-12 13:37:49', '2017-02-12 13:37:49', '', '0', '" + post_guid + "', '0', '" + post_type +"', '', '1')"
        self.query(qpost)

    def get_translite(self, tstring):
        return translit.translify(tstring.decode('utf-8')).replace("'","").replace(" ","_").lower().encode('utf-8')


    def check_post_name(self, post_name):
        for x in self.fetch("select post_name from `wp_posts`"):
            if(post_name == x[0]):
                return False
        return True

    def delete_post(self, id = ""):
        if id == "":
            id = self.fetch("select id from `wp_posts` order by id desc limit 1")[0][0]
        self.query("delete from `wp_posts` where id = " + str(id))
