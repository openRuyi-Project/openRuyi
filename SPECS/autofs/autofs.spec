# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           autofs
Version:        5.1.9
Release:        %autorelease
Summary:        A tool from automatically mounting and umounting filesystems.
License:        GPL-2.0-or-later
URL:            https://docs.kernel.org/filesystems/autofs.html
VCS:            git:https://git.kernel.org/pub/scm/linux/storage/autofs/autofs.git
#!RemoteAsset
Source:         https://www.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         autofs-5.1.9-Fix-incompatible-function-pointer-types-in-cyrus-sasl-module.patch

BuildOption(conf):  --with-systemd
BuildOption(conf):  --disable-mount-locking
BuildOption(conf):  --enable-ignore-busy
BuildOption(conf):  --enable-force-shutdown
BuildOption(conf):  --without-hesiod
BuildOption(conf):  --with-libtirpc
BuildOption(build):  DONTSTRIP=1

BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libnsl)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  m4
BuildRequires:  bison
BuildRequires:  flex
#BuildRequires:  openldap2-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  openssl-devel
BuildRequires:  util-linux
BuildRequires:  krb5-devel

Requires:       /usr/bin/bash
Requires:       sed
Requires:       grep
Requires:       /usr/bin/ps

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%conf -p
autoreconf -fiv

%install
install -d -m 755 $RPM_BUILD_ROOT%{_unitdir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/autofs
mkdir -p -m755 $RPM_BUILD_ROOT%{_mandir}/{man5,man8}
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/auto.master.d

make install mandir=%{_mandir} INSTALLROOT=$RPM_BUILD_ROOT
echo make -C redhat
make -C redhat
install -m 644 redhat/autofs.service $RPM_BUILD_ROOT%{_unitdir}/autofs.service
install -m 644 redhat/autofs.conf $RPM_BUILD_ROOT%{_sysconfdir}/autofs.conf
install -m 644 redhat/autofs.sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/autofs
install -m 644 samples/auto.master $RPM_BUILD_ROOT%{_sysconfdir}/auto.master
install -m 644 samples/auto.misc $RPM_BUILD_ROOT%{_sysconfdir}/auto.misc
install -m 755 samples/auto.net $RPM_BUILD_ROOT%{_sysconfdir}/auto.net
install -m 755 samples/auto.smb $RPM_BUILD_ROOT%{_sysconfdir}/auto.smb
install -m 600 samples/autofs_ldap_auth.conf $RPM_BUILD_ROOT%{_sysconfdir}/autofs_ldap_auth.conf

# No tests.
%check

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%defattr(-,root,root)
%doc CREDITS CHANGELOG INSTALL COPY* README* samples/ldap* samples/*.schema
%doc samples/am-utils-ldap-id.txt samples/autofs_ldap_auth.conf
%config %{_unitdir}/autofs.service
%config(noreplace) %{_sysconfdir}/auto.master
%config(noreplace) %{_sysconfdir}/autofs.conf
%config(noreplace,missingok) %{_sysconfdir}/auto.misc
%config(noreplace,missingok) %{_sysconfdir}/auto.net
%config(noreplace,missingok) %{_sysconfdir}/auto.smb
%config(noreplace) %{_sysconfdir}/sysconfig/autofs
%config(noreplace) %{_sysconfdir}/autofs_ldap_auth.conf
%{_sbindir}/automount
%{_libdir}/libautofs.so
%dir %{_libdir}/autofs
%{_libdir}/autofs/*
%{_mandir}/*/*
%dir %{_sysconfdir}/auto.master.d

%changelog
%autochangelog
