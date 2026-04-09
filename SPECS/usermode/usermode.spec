# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           usermode
Version:        1.114
Release:        %autorelease
Summary:        Tools for certain user account management tasks
License:        GPL-2.0-or-later
URL:            https://pagure.io/usermode
VCS:            git:https://pagure.io/usermode
#!RemoteAsset
Source0:        https://releases.pagure.org/usermode/usermode-%{version}.tar.xz
Source1:        config-util
BuildSystem:    autotools

BuildOption(conf):  --without-selinux
BuildOption(conf):  --without-fexecve
BuildOption(conf):  --without-gtk

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  util-linux
BuildRequires:  pkgconfig(libuser)
BuildRequires:  pkgconfig(pam)

Requires:       pam
Requires:       shadow
Requires:       util-linux

%description
The usermode package contains the userhelper program, which can be
used to allow configured programs to be run with superuser privileges
by ordinary users.

%install -a
mkdir -p %{buildroot}/etc/security/console.apps
install -p -m 644 %{SOURCE1} %{buildroot}/etc/security/console.apps/config-util

%install -a
# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc ChangeLog NEWS README
%attr(4711,root,root) %{_sbindir}/userhelper
%{_bindir}/consolehelper
%{_mandir}/man8/userhelper.8*
%{_mandir}/man8/consolehelper.8*
%dir /etc/security/console.apps
%config(noreplace) %{_sysconfdir}/security/console.apps/config-util

%changelog
%autochangelog
