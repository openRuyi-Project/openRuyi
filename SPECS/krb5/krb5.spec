# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

# default without systemd
%bcond systemd 0

Name:           krb5
Version:        1.22.1
Release:        %autorelease
Summary:        The Kerberos 5 network authentication system
License:        MIT
URL:            https://web.mit.edu/kerberos/
#!RemoteAsset
Source:         https://kerberos.org/dist/krb5/1.22/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --without-ldap
BuildOption(conf): --disable-static --enable-dns-for-realm --disable-rpath
BuildOption(conf): --with-pam --enable-pkinit --with-crypto-impl=openssl --with-selinux
BuildOption(conf): --with-system-et --with-system-ss --with-system-verto --with-lmdb
BuildOption(conf): --localstatedir=%{_localstatedir}

BuildOption(build): -C src
BuildOption(install): -C src

BuildRequires:  autoconf bison keyutils-devel
BuildRequires:  pam-devel pkgconfig pkgconfig(com_err) pkgconfig(libselinux)
BuildRequires:  pkgconfig(libssl) pkgconfig(libverto) pkgconfig(lmdb)
BuildRequires:  pkgconfig(ss)

%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%endif

%if %{with systemd}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%endif

%description
Kerberos is a network authentication system. This package contains all the
core libraries, clients, servers, and plugins.

%package        devel
Summary:        Development files for MIT Kerberos 5
Requires:       %{name} = %{version}
Requires:       keyutils-devel pkgconfig(com_err) pkgconfig(libverto) pkgconfig(ss)

%description    devel
This package contains the libraries, header files, and documentation needed
for developing applications that use Kerberos 5.

%conf
cd src
export DEFCCNAME=DIR:/run/user/%%{uid}/krb5cc
autoreconf -fi
%configure

%install -a
find %{buildroot} -type f -name "*.la" -delete -print
install -D -m 644 src/util/ac_check_krb5.m4 %{buildroot}%{_datadir}/aclocal/ac_check_krb5.m4
install -d -m 755 %{buildroot}%{_sysconfdir}/krb5.conf.d

install -d -m 700 %{buildroot}%{_localstatedir}/kerberos/krb5kdc

install -m 644 src/config-files/krb5.conf %{buildroot}%{_sysconfdir}/krb5.conf
install -m 644 src/config-files/kdc.conf %{buildroot}%{_sysconfdir}/kdc.conf

# remove some files should not in krb5
rm -rf %{buildroot}%{_bindir}/compile_et
rm -rf %{buildroot}%{_includedir}/com_err.h
rm -rf %{buildroot}%{_libdir}/libcom_err.so
rm -rf %{buildroot}%{_datadir}/et/

%if %{with systemd}
%post
%systemd_post kadmind.service kpropd.service
%preun
%systemd_preun kadmind.service kpropd.service
%postun
%systemd_postun_with_restart kadmind.service kpropd.service
%endif

%files
%license doc/notice.rst
%doc doc/
%config(noreplace) %{_sysconfdir}/kdc.conf
%config(noreplace) %{_sysconfdir}/krb5.conf
%dir %{_sysconfdir}/krb5.conf.d
%dir %attr(0700,root,root) %{_localstatedir}/kerberos
%dir %attr(0700,root,root) %{_localstatedir}/kerberos/krb5kdc
%{_libdir}/lib*.so.*
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%{_libdir}/krb5/plugins/*/*.so
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%exclude %{_mandir}/man1/compile_et.1.gz
%exclude %{_mandir}/man1/krb5-config.1*
%exclude %{_mandir}/man5/.k5identity.5.gz
%exclude %{_mandir}/man5/.k5login.5.gz
%{_datadir}/locale/*/LC_MESSAGES/mit-krb5.mo
%dir %{_datadir}/examples
%dir %{_datadir}/examples/krb5
%{_datadir}/examples/krb5/*

%files devel
%{_includedir}/gssapi/
%{_includedir}/gssrpc/
%{_includedir}/kadm5/
%{_includedir}/kdb.h
%{_includedir}/krad.h
%{_includedir}/krb5.h
%{_includedir}/krb5/*
%{_includedir}/gssapi.h
%{_includedir}/profile.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_bindir}/krb5-config
%{_datadir}/aclocal/ac_check_krb5.m4
%{_mandir}/man1/krb5-config.1*
%{_mandir}/man5/.k5identity.5.gz
%{_mandir}/man5/.k5login.5.gz

%changelog
%{?autochangelog}
