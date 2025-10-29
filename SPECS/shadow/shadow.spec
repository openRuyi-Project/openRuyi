# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global includesubiddir %{_includedir}/shadow

Name:          shadow
Version:       4.18.0
Release:       %autorelease
Summary:       User and group account management utilities
License:       BSD-3-Clause AND GPL-2.0-or-later
URL:           https://github.com/shadow-maint/shadow
#!RemoteAsset
Source0:       https://github.com/shadow-maint/shadow/releases/download/%{version}/%{name}-%{version}.tar.xz

Source1:       useradd.defaults
Source2:       login.defs
Source3:       shadow.timer
Source4:       shadow.service
Source5:       passwd.service

Patch0:        0001-openruyi-disable-conflicting-tools.patch
Patch1:        0002-openruyi-adapt-configs.patch

BuildSystem:   autotools

# Configure options for a modern, systemd-centric distro.
BuildOption(conf): --enable-shadowgrp
BuildOption(conf): --with-audit
BuildOption(conf): --with-libpam
BuildOption(conf): --with-acl
BuildOption(conf): --with-attr
BuildOption(conf): --with-selinux
# Enable modern password hashing algorithms.
BuildOption(conf): --with-sha-crypt
BuildOption(conf): --with-yescrypt
BuildOption(conf): --without-libbsd
BuildOption(conf): --without-libcrack
BuildOption(conf): --without-nscd
BuildOption(conf): --without-sssd
# --- CRITICAL: Disable tools provided by util-linux/systemd ---
BuildOption(conf): --without-su
BuildOption(conf): --disable-account-tools-setuid
BuildOption(conf): --with-group-name-max-length=32
BuildOption(conf): --sbindir=%{_bindir}

BuildOption(install): gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale
BuildOption(install): MKINSTALLDIRS=`pwd`/mkinstalldirs

BuildRequires: make, gcc, autoconf, automake, libtool
BuildRequires: audit-devel, acl-devel, libattr-devel, pam-devel
BuildRequires: libselinux-devel, libsemanage-devel, libxcrypt-devel

Requires:      audit, acl, libattr, pam, libxcrypt
# Requires the subid library, which is part of this source package.
Requires:      subid%{?_isa} = %{version}-%{release}

Requires:      setup

Provides: shadow = %{version}-%{release}
Provides: passwd = 0.80-18
Obsoletes: passwd <= 0.80-19

%description
This package includes the necessary programs for managing user and group
accounts, and their passwords and groups in shadow format.

# --- Library Subpackage for Subordinate IDs ---
%package -n subid
Summary:       A library to manage subordinate UID and GID ranges

%description -n subid
The subid library provides a way to manage subordinate ID ranges,
primarily used for unprivileged containers.

# --- Development Package ---
%package devel
Summary:       Development files for shadow and subid
Requires:      subid%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries for
shadow and subid.

%conf -p
autoreconf -fiv

%install -a
%make_install -C man install-man

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/default
install -p -c -m 0600 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/default/useradd
install -p -c -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/login.defs
install -d -m 755 $RPM_BUILD_ROOT%{_pam_confdir}
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_pam_confdir}/passwd

# --- CRITICAL: Ensure conflicting tools are removed ---
rm -f %{buildroot}%{_bindir}/{su,login,chfn,chsh,expiry,faillog}
rm -f %{buildroot}%{_sbindir}/{nologin,logoutd}

# Also remove corresponding man pages and PAM configs to be safe
rm -f %{buildroot}%{_mandir}/man1/{su,login,chfn,chsh,expiry,faillog}.1*
rm -f %{buildroot}%{_mandir}/man8/{nologin,logoutd}.8*
rm -f %{buildroot}%{_sysconfdir}/pam.d/{su,login,chfn,chsh}

find $RPM_BUILD_ROOT%{_mandir} -depth -type d -empty -delete

%find_lang %{name} --generate-subpackages --with-man --all-name

echo $(ls)
mkdir -p $RPM_BUILD_ROOT/%{includesubiddir}
install -m 644 libsubid/subid.h $RPM_BUILD_ROOT/%{includesubiddir}/

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a

install -Dm644 %{SOURCE3} %{buildroot}%{_unitdir}/shadow.timer
install -Dm644 %{SOURCE4} %{buildroot}%{_unitdir}/shadow.service

# touch %{buildroot}%{_sysconfdir}/subuid
# touch %{buildroot}%{_sysconfdir}/subgid


%post
%systemd_post shadow.service shadow.timer

%preun
%systemd_preun shadow.service shadow.timer

%postun
%systemd_postun shadow.service shadow.timer

%ldconfig_scriptlets -n subid

%files
%doc NEWS doc/HOWTO README
# %config(noreplace) %attr(0600,root,root) %{_sysconfdir}/subgid
# %config(noreplace) %attr(0600,root,root) %{_sysconfdir}/subuid
%attr(0644,root,root)   %config(noreplace) %{_sysconfdir}/login.defs
%attr(0644,root,root)   %config(noreplace) %{_sysconfdir}/default/useradd

%config(noreplace) %{_pam_confdir}/passwd
%config(noreplace) %{_pam_confdir}/chpasswd
%config(noreplace) %{_pam_confdir}/groupmems
%config(noreplace) %{_pam_confdir}/newusers

%{_unitdir}/shadow.service
%{_unitdir}/shadow.timer

%{_bindir}/sg
%attr(4755,root,root) %{_bindir}/chage
%attr(4755,root,root) %{_bindir}/gpasswd
%attr(0755,root,root) %caps(cap_setgid=ep) %{_bindir}/newgidmap
%attr(0755,root,root) %caps(cap_setuid=ep) %{_bindir}/newuidmap
%attr(4755,root,root) %{_bindir}/passwd
%{_bindir}/chgpasswd
%{_bindir}/chpasswd
%{_bindir}/group*
%{_bindir}/grp*
%{_bindir}/lastlog
%{_bindir}/newusers
%{_bindir}/pwck
%{_bindir}/pwconv
%{_bindir}/pwunconv
%{_bindir}/user*

%{_mandir}/man1/chage.1*
%{_mandir}/man1/gpasswd.1*
%{_mandir}/man1/sg.1*
%{_mandir}/man1/newgidmap.1*
%{_mandir}/man1/newuidmap.1*
%{_mandir}/man1/passwd.1*
%{_mandir}/man3/getspnam.3*
%{_mandir}/man3/shadow.3*
%{_mandir}/man5/faillog.5*
%{_mandir}/man5/gshadow.5*
%{_mandir}/man5/login.defs.5*
%{_mandir}/man5/passwd.5*
%{_mandir}/man5/shadow.5*
%{_mandir}/man5/subgid.5*
%{_mandir}/man5/subuid.5*
%{_mandir}/man8/*conv.8*
%{_mandir}/man8/chgpasswd.8*
%{_mandir}/man8/chpasswd.8*
%{_mandir}/man8/faillog.8*
%{_mandir}/man8/group*.8*
%{_mandir}/man8/grpck.8*
%{_mandir}/man8/lastlog.8*
%{_mandir}/man8/newusers.8*
%{_mandir}/man8/pwck.8*
%{_mandir}/man8/user*.8*

%files -n subid
%{_libdir}/libsubid.so.*
%{_bindir}/getsubids
%{_mandir}/man1/getsubids.1*

%files devel
%{includesubiddir}/subid.h
%{_libdir}/libsubid.so

%changelog
%{?autochangelog}
