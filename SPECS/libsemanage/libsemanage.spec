# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsemanage
Version:        3.9
Release:        %autorelease
Summary:        SELinux policy management library and utilities
License:        LGPL-2.1-or-later
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
#!RemoteAsset
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        semanage.conf
BuildSystem:    autotools

BuildRequires:  audit-devel bison flex bzip2-devel libselinux-devel libsepol-devel
BuildRequires:  pkgconfig make gcc


BuildOption(build): CFLAGS="%{optflags} -fno-semantic-interposition"
BuildOption(build): LIBDIR="%{_libdir}"
BuildOption(build): LIBEXECDIR="%{_libexecdir}"
BuildOption(build): SHLIBDIR="%{_libdir}"

BuildOption(install): LIBDIR="%{_libdir}"
BuildOption(install): LIBEXECDIR="%{_libexecdir}"
BuildOption(install): SHLIBDIR="%{_libdir}"

%description
libsemanage is the SELinux policy management library. It is used to
manipulate SELinux policies. This package contains the runtime library,
configuration files, and policy migration tools.

%package devel
Summary:        Development files for the SELinux policy management library
Requires:       %{name} = %{version}

%description devel
The libsemanage-devel package contains the header files, static and shared
libraries needed for developing applications that manipulate SELinux policies.

%prep -a
grep /usr/libexec . -rl | xargs sed -i "s|/usr/libexec|%{_libexecdir}|g"

# No configure
%conf

%install -a
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/selinux/semanage.conf
install -d -m 755 %{buildroot}%{_localstatedir}/lib/selinux

find %{buildroot} -type f -name "*.la" -delete -print

%files
%license LICENSE
%{_libdir}/libsemanage.so.*
%dir %{_localstatedir}/lib/selinux
%dir %{_libexecdir}/selinux
%{_libexecdir}/selinux/*
%dir %{_sysconfdir}/selinux
%config(noreplace) %{_sysconfdir}/selinux/semanage.conf

%files devel
%{_libdir}/libsemanage.so
%{_libdir}/libsemanage.a
%{_libdir}/pkgconfig/libsemanage.pc
%{_includedir}/semanage/
%{_mandir}/man3/*
%{_mandir}/man5/*

%changelog
%{?autochangelog}
