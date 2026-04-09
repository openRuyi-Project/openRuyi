# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global nginx_moduledir %{_libdir}/nginx/modules
%global nginx_moduleconfdir %{_datadir}/nginx/modules

Name:           nginx
Version:        1.28.0
Release:        %autorelease
Summary:        High performance web server and reverse proxy server
License:        BSD-2-Clause
URL:            https://nginx.org
VCS:            git:https://github.com/nginx/nginx.git
#!RemoteAsset
Source0:        https://nginx.org/download/nginx-%{version}.tar.gz
Source1:        nginx.service
Source2:        nginx.logrotate
Source3:        nginx.sysusers

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros

Provides:       webserver

Requires:       openssl
Requires:       pcre2
Requires:       zlib
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Nginx is a web server and a reverse proxy server for HTTP, SMTP, POP3 and
IMAP protocols, with a strong focus on high concurrency, performance and low
memory usage.

%package        doc
Summary:        Documentation and examples for nginx
BuildArch:      noarch

%description    doc
This package contains documentation, man pages, vim syntax files, and
example HTML files for nginx web server.

%prep
%autosetup -n nginx-%{version}

# nginx does not utilize a standard configure script.
%conf
./configure \
    --prefix=/etc/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --sbin-path=/usr/bin/nginx \
    --modules-path=%{_libdir}/nginx/modules \
    --pid-path=/run/nginx.pid \
    --lock-path=/run/lock/nginx.lock \
    --user=nginx \
    --group=nginx \
    --http-log-path=/var/log/nginx/access.log \
    --error-log-path=/var/log/nginx/error.log \
    --http-client-body-temp-path=/var/lib/nginx/client-body \
    --http-proxy-temp-path=/var/lib/nginx/proxy \
    --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
    --http-scgi-temp-path=/var/lib/nginx/scgi \
    --http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
    --with-compat \
    --with-file-aio \
    --with-threads \
    --with-http_addition_module \
    --with-http_auth_request_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_mp4_module \
    --with-http_random_index_module \
    --with-http_realip_module \
    --with-http_secure_link_module \
    --with-http_slice_module \
    --with-http_ssl_module \
    --with-http_stub_status_module \
    --with-http_sub_module \
    --with-http_v2_module \
    --with-http_v3_module \
    --with-pcre-jit \
    --with-stream \
    --with-stream_realip_module \
    --with-stream_ssl_module \
    --with-stream_ssl_preread_module \
    --with-cc-opt="%{optflags}" \
    --with-ld-opt="%{build_ldflags}"

%build

%make_build

%install
%make_install

# Install systemd service file
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/nginx.service

# Install logrotate configuration
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/nginx

# Create directories
install -d -m 0755 %{buildroot}/var/lib/nginx
install -d -m 0700 %{buildroot}/var/lib/nginx/proxy
install -d -m 0700 %{buildroot}/var/lib/nginx/client-body
install -d -m 0700 %{buildroot}/var/lib/nginx/fastcgi
install -d -m 0700 %{buildroot}/var/lib/nginx/scgi
install -d -m 0700 %{buildroot}/var/lib/nginx/uwsgi
install -d -m 0755 %{buildroot}/var/log/nginx

# Move html directory to standard location
install -d %{buildroot}%{_datadir}/nginx
mv %{buildroot}/etc/nginx/html %{buildroot}%{_datadir}/nginx/

# Update nginx.conf to point to new html location
sed -i 's|root\s*html;|root   /usr/share/nginx/html;|g' \
    %{buildroot}%{_sysconfdir}/nginx/nginx.conf

# Remove .default files
rm -f %{buildroot}%{_sysconfdir}/nginx/*.default

# Install man page
install -p -D -m 0644 objs/nginx.8 %{buildroot}%{_mandir}/man8/nginx.8

# Install vim syntax files
for i in ftdetect ftplugin indent syntax; do
    install -p -D -m 0644 contrib/vim/${i}/nginx.vim \
        %{buildroot}%{_datadir}/vim/vimfiles/${i}/nginx.vim
done

install -p -d -m 0755 %{buildroot}%{nginx_moduleconfdir}
install -p -d -m 0755 %{buildroot}%{nginx_moduledir}

# install sysusers file
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
%systemd_post nginx.service

%preun
%systemd_preun nginx.service

%postun
%systemd_postun_with_restart nginx.service

%files
%license LICENSE
%{_bindir}/nginx
%dir %{_sysconfdir}/nginx
%config(noreplace) %{_sysconfdir}/nginx/fastcgi.conf
%config(noreplace) %{_sysconfdir}/nginx/fastcgi_params
%config(noreplace) %{_sysconfdir}/nginx/koi-utf
%config(noreplace) %{_sysconfdir}/nginx/koi-win
%config(noreplace) %{_sysconfdir}/nginx/mime.types
%config(noreplace) %{_sysconfdir}/nginx/nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/scgi_params
%config(noreplace) %{_sysconfdir}/nginx/uwsgi_params
%config(noreplace) %{_sysconfdir}/nginx/win-utf
%config(noreplace) %{_sysconfdir}/logrotate.d/nginx
%{_sysusersdir}/%{name}.conf
%dir %{_libdir}/nginx
%dir %{_libdir}/nginx/modules
%{_unitdir}/nginx.service
%dir %attr(755,nginx,nginx) /var/lib/nginx
%dir %attr(700,nginx,nginx) /var/lib/nginx/client-body
%dir %attr(700,nginx,nginx) /var/lib/nginx/fastcgi
%dir %attr(700,nginx,nginx) /var/lib/nginx/proxy
%dir %attr(700,nginx,nginx) /var/lib/nginx/scgi
%dir %attr(700,nginx,nginx) /var/lib/nginx/uwsgi
%dir %attr(755,nginx,nginx) /var/log/nginx

%files doc
%doc CHANGES
%{_datadir}/nginx/html/*
%{_datadir}/vim/vimfiles/ftdetect/nginx.vim
%{_datadir}/vim/vimfiles/ftplugin/nginx.vim
%{_datadir}/vim/vimfiles/indent/nginx.vim
%{_datadir}/vim/vimfiles/syntax/nginx.vim
%{_mandir}/man8/nginx.8*

%changelog
%autochangelog
