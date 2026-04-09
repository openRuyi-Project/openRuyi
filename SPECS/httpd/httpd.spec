# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define contentdir %{_datadir}/httpd
%define docroot /var/www
%define suexec_caller apache
# MMN (Module Magic Number) from ap_mmn.h
# Used to guarantee ABI compatibility for loadable modules
# Extracted from: include/ap_mmn.h (MODULE_MAGIC_NUMBER_MAJOR)
# Verify: echo MODULE_MAGIC_NUMBER_MAJOR | cpp -include include/ap_mmn.h | sed -n '/^2/p'
%define mmn 20120211
%define mmnisa %{mmn}%{__isa_name}%{__isa_bits}

Name:           httpd
Version:        2.4.66
Release:        %autorelease
Summary:        Apache HTTP Server
License:        Apache-2.0
URL:            https://httpd.apache.org/
VCS:            git:https://github.com/apache/httpd.git
#!RemoteAsset
Source0:        https://www.apache.org/dist/httpd/httpd-%{version}.tar.bz2
Source1:        config.layout
Source2:        httpd.sysusers
Source3:        httpd.tmpfiles
Source4:        httpd.logrotate
Source5:        httpd.service
BuildSystem:    autotools

BuildOption(conf):  --prefix=%{_sysconfdir}/httpd
BuildOption(conf):  --exec-prefix=%{_prefix}
BuildOption(conf):  --bindir=%{_bindir}
BuildOption(conf):  --sbindir=%{_sbindir}
BuildOption(conf):  --mandir=%{_mandir}
BuildOption(conf):  --libdir=%{_libdir}
BuildOption(conf):  --sysconfdir=%{_sysconfdir}/httpd/conf
BuildOption(conf):  --includedir=%{_includedir}/httpd
BuildOption(conf):  --libexecdir=%{_libdir}/httpd/modules
BuildOption(conf):  --datadir=%{contentdir}
BuildOption(conf):  --with-installbuilddir=%{_libdir}/httpd/build
BuildOption(conf):  --enable-layout=openRuyi
BuildOption(conf):  --enable-mpms-shared=all
BuildOption(conf):  --with-apr=%{_prefix}
BuildOption(conf):  --with-apr-util=%{_prefix}
BuildOption(conf):  --enable-suexec
BuildOption(conf):  --with-suexec
BuildOption(conf):  --enable-suexec-capabilities
BuildOption(conf):  --with-suexec-caller=%{suexec_caller}
BuildOption(conf):  --with-suexec-docroot=%{docroot}
BuildOption(conf):  --without-suexec-logfile
BuildOption(conf):  --with-suexec-syslog
BuildOption(conf):  --with-suexec-bin=%{_sbindir}/suexec
BuildOption(conf):  --with-suexec-uidmin=1000
BuildOption(conf):  --with-suexec-gidmin=1000
BuildOption(conf):  --with-brotli
BuildOption(conf):  --enable-pie
BuildOption(conf):  --with-pcre2=%{_bindir}/pcre2-config
BuildOption(conf):  --enable-mods-shared=all
BuildOption(conf):  --enable-ssl
BuildOption(conf):  --with-ssl
BuildOption(conf):  --disable-distcache
BuildOption(conf):  --enable-proxy
BuildOption(conf):  --enable-proxy-fdpass
BuildOption(conf):  --enable-cache
BuildOption(conf):  --enable-disk-cache
BuildOption(conf):  --enable-ldap
BuildOption(conf):  --enable-authnz-ldap
BuildOption(conf):  --enable-cgid
BuildOption(conf):  --enable-cgi
BuildOption(conf):  --enable-authnz-fcgi
BuildOption(conf):  --enable-cgid-fdpassing
BuildOption(conf):  --enable-authn-anon
BuildOption(conf):  --enable-authn-alias
BuildOption(conf):  --enable-systemd=static
BuildOption(conf):  --disable-imagemap
BuildOption(conf):  --disable-file-cache
BuildOption(conf):  --disable-http2
BuildOption(conf):  --disable-md
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  findutils
BuildRequires:  xmlto
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(apr-1) >= 1.5.0
BuildRequires:  pkgconfig(apr-util-1) >= 1.5.0
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  systemd-rpm-macros

# Add after we have openruyi-logos
# Requires:       system-logos-httpd
# Add after we have
# Requires:       /etc/mime.types
Recommends:     mod_http2

Provides:       webserver
Provides:       mod_dav = %{version}-%{release}
Provides:       httpd-suexec = %{version}-%{release}
Provides:       httpd-mmn = %{mmn}
Provides:       httpd-mmn = %{mmnisa}
%{?systemd_requires}

%description
The Apache HTTP Server Project is an effort to develop and maintain an
open-source HTTP server for modern operating systems including UNIX and
Windows. The goal of this project is to provide a secure, efficient and
extensible server that provides HTTP services in sync with the current
HTTP standards.

%package        devel
Summary:        Development interfaces for the Apache HTTP server.
Requires:       pkgconfig(apr-1) >= 1.5.0
Requires:       pkgconfig(apr-util-1) >= 1.5.0
Requires:       libtool
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The httpd-devel package contains the APXS binary and other files
that you need to build Dynamic Shared Objects (DSOs) for the
Apache HTTP Server.

If you are installing the Apache HTTP server and you want to be
able to compile or develop additional modules for Apache, you need
to install this package.

%package        tools
Summary:        Tools for use with the Apache HTTP Server

%description    tools
The httpd-tools package contains tools which can be used with
the Apache HTTP Server.

%prep -a
cat %{_sourcedir}/config.layout >> config.layout

# set default user
sed -e "s#User daemon#User %{suexec_caller}#" \
    -e "s#Group daemon#Group %{suexec_caller}#" \
    -i docs/conf/httpd.conf.in

# Prevent use of setcap in "install-suexec-caps" target.
sed -i '/suexec/s,setcap ,echo Skipping setcap for ,' Makefile.in

%install -a
# Install systemd service files
mkdir -p %{buildroot}%{_unitdir}
install -p -m644 %{_sourcedir}/httpd.service %{buildroot}%{_unitdir}/httpd.service

# Fix content dir in sysusers file and install it
install -p -D -m 0644 %{_sourcedir}/httpd.sysusers %{buildroot}%{_sysusersdir}/httpd.conf

# tmpfiles.d configuration
mkdir -p  %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 644 -p %{_sourcedir}/httpd.tmpfiles %{buildroot}%{_prefix}/lib/tmpfiles.d/httpd.conf

# Install logrotate config
mkdir -p %{buildroot}/etc/logrotate.d
install -m 644 -p %{_sourcedir}/httpd.logrotate %{buildroot}/etc/logrotate.d/httpd

mkdir -p %{buildroot}%{_localstatedir}/log/httpd \
         %{buildroot}%{_localstatedir}/lib/httpd

# Create cache directory
mkdir -p %{buildroot}%{_localstatedir}/cache/httpd \
         %{buildroot}%{_localstatedir}/cache/httpd/proxy \
         %{buildroot}%{_localstatedir}/cache/httpd/ssl

# Make the MMN accessible to module packages
echo %{mmnisa} > %{buildroot}%{_includedir}/httpd/.mmn

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.httpd <<EOF
%%_httpd_mmn %{mmnisa}
%%_httpd_confdir %%{_sysconfdir}/httpd/conf.d
%%_httpd_contentdir %{contentdir}
%%_httpd_moddir %%{_libdir}/httpd/modules
%%_httpd_requires Requires: httpd-mmn = %%{_httpd_mmn}
%%_httpd_statedir %%{_localstatedir}/lib/httpd
EOF

# symlinks for /etc/httpd
ln -s ../..%{_localstatedir}/log/httpd %{buildroot}/etc/httpd/logs
ln -s ../..%{_localstatedir}/lib/httpd %{buildroot}/etc/httpd/state
ln -s ../..%{_libdir}/httpd/modules %{buildroot}/etc/httpd/modules
ln -s /run/httpd %{buildroot}/etc/httpd/run

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d

cat %{buildroot}%{_sysconfdir}/httpd/conf/httpd.conf
# set sane defaults
sed -e 's#/usr/lib/httpd/modules/#modules/#' \
    -e 's|#\(LoadModule negotiation_module \)|\1|' \
    -e 's|#\(LoadModule include_module \)|\1|' \
    -e 's|#\(LoadModule userdir_module \)|\1|' \
    -e 's|#\(LoadModule slotmem_shm_module \)|\1|' \
    -e 's|#\(Include conf/extra/httpd-multilang-errordoc.conf\)|\1|' \
    -e 's|#\(Include conf/extra/httpd-autoindex.conf\)|\1|' \
    -e 's|#\(Include conf/extra/httpd-languages.conf\)|\1|' \
    -e 's|#\(Include conf/extra/httpd-userdir.conf\)|\1|' \
    -e 's|#\(Include conf/extra/httpd-default.conf\)|\1|' \
    -e 's|#\(Include conf/extra/httpd-mpm.conf\)|\1|' \
    -i "%{buildroot}%{_sysconfdir}/httpd/conf/httpd.conf"

# allow optional drop-in conf files for local configuration
echo "IncludeOptional conf.d/*.conf" >> %{buildroot}%{_sysconfdir}/httpd/conf/httpd.conf

ls -al %{buildroot}%{_sysconfdir}/httpd/conf/extra/
cat %{buildroot}%{_sysconfdir}/httpd/conf/httpd.conf

rm -rf %{buildroot}/etc/httpd/conf/original \
       %{buildroot}%{_libdir}/httpd/build/config.nice \
       %{buildroot}%{_libdir}/httpd/modules/*.exp \
       %{buildroot}%{docroot}/html/*.html \
       %{buildroot}%{docroot}/cgi-bin/* \

# No tests
%check

%pre
%sysusers_create_package %{name} %{SOURCE2}

%post
%systemd_post httpd.service

%preun
%systemd_preun httpd.service

%postun
%systemd_postun httpd.service

%files
%license LICENSE NOTICE
%doc ABOUT_APACHE README CHANGES VERSIONING
%doc docs/conf/extra/*.conf
%{_sysconfdir}/httpd/modules
%{_sysconfdir}/httpd/logs
%{_sysconfdir}/httpd/state
%{_sysconfdir}/httpd/run
%dir %{_sysconfdir}/httpd
%dir %{_sysconfdir}/httpd/conf.d
%dir %{_sysconfdir}/httpd/conf
%config(noreplace) %{_sysconfdir}/httpd/conf/{httpd.conf,magic}
%config(noreplace) %{_sysconfdir}/httpd/conf/extra/*.conf
%config %{_sysconfdir}/httpd/conf/mime.types
%config(noreplace) %{_sysconfdir}/logrotate.d/httpd
%dir %{_libdir}/httpd
%dir %{_libdir}/httpd/modules
%{_libdir}/httpd/modules/mod*.so
%{_sbindir}/fcgistarter
%{_sbindir}/htcacheclean
%{_sbindir}/httpd
%{_sbindir}/apachectl
%{_sbindir}/checkgid
%{_sbindir}/envvars
%{_sbindir}/envvars-std
%{_sbindir}/rotatelogs
%caps(cap_setuid,cap_setgid+pe) %attr(0510,root,%{suexec_caller}) %{_sbindir}/suexec
%{_unitdir}/httpd.service
%{_sysusersdir}/httpd.conf
%{_prefix}/lib/tmpfiles.d/httpd.conf
%attr(0710,root,apache) %dir /run/httpd
%attr(0700,root,root) %dir %{_localstatedir}/log/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/lib/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/cache/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/cache/httpd/proxy
%attr(0700,apache,root) %dir %{_localstatedir}/cache/httpd/ssl
%dir %{docroot}
%dir %{docroot}/cgi-bin
%dir %{docroot}/html
%dir %{contentdir}
%dir %{contentdir}/icons
%{contentdir}/icons/*
%dir %{contentdir}/error
%dir %{contentdir}/error/include
%{contentdir}/error/README
%{contentdir}/error/*.var
%{contentdir}/error/include/*.html
%{contentdir}/manual
%{_mandir}/man8/*

%files devel
%{_includedir}/httpd
%{_bindir}/apxs
%{_bindir}/dbmmanage
%{_mandir}/man1/apxs.1*
%{_mandir}/man1/dbmmanage.1*
%dir %{_libdir}/httpd/build
%{_libdir}/httpd/build/*.mk
%{_libdir}/httpd/build/*.sh
%{_rpmconfigdir}/macros.d/macros.httpd

%files tools
%license LICENSE NOTICE
%{_bindir}/ab
%{_bindir}/htdbm
%{_bindir}/htdigest
%{_bindir}/httxt2dbm
%{_bindir}/htpasswd
%{_bindir}/logresolve
%{_mandir}/man1/*
%doc LICENSE NOTICE
%exclude %{_bindir}/apxs
%exclude %{_mandir}/man1/apxs.1*
%exclude %{_mandir}/man1/dbmmanage.1*

%changelog
%autochangelog
