# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Summary:        Locate files on the file system
Name:           mlocate
Version:        0.26
Release:        %autorelease
License:        GPL-2.0-only
URL:            https://pagure.io/mlocate
#!RemoteAsset
Source0:        http://releases.pagure.org/mlocate/mlocate-%{version}.tar.xz
Source1:        mlocate.sysusers
BuildSystem:    autotools

BuildOption(conf):  --localstatedir=%{_localstatedir}/lib

BuildRequires:  xz
BuildRequires:  sed
BuildRequires:  grep
BuildRequires:  autoconf
BuildRequires:  automake

%description
A new locate implementation. The m character stands for merging,
because updatedb reuses the existing database to avoid re-reading
most of the file system.

%conf -p
autoreconf -fiv

%install -a
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*

%find_lang %{name} --generate-subpackages
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf
touch %{buildroot}%{_localstatedir}/lib/mlocate/mlocate.db

%pre
%sysusers_create_package %{name} %{SOURCE1}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/locate
%{_bindir}/updatedb
%{_mandir}/man*/*
%{_sysusersdir}/%{name}.conf
%dir %attr(0750,root,mlocate) %{_localstatedir}/lib/mlocate
%ghost %attr(0640,root,mlocate) %{_localstatedir}/lib/mlocate/mlocate.db

%changelog
%autochangelog
