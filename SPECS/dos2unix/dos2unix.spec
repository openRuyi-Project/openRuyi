# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dos2unix
Version:        7.5.3
Release:        %autorelease
Summary:        Text file format converters
License:        BSD-3-Clause
URL:            https://waterlan.home.xs4all.nl/dos2unix.html
# VCS: No VCS link available
#!RemoteAsset
Source:         https://waterlan.home.xs4all.nl/dos2unix/dos2unix-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):   LDFLAGS="%{build_ldflags}" prefix=%{_prefix}
BuildOption(install):  prefix=%{_prefix}

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make

Provides:       unix2dos = %{version}-%{release}

%description
Convert text files with DOS or Mac line endings to Unix line endings and
vice versa.

# No configure
%conf

%install -a
# We add doc files manually to %%doc
rm -rf %{buildroot}%{_docdir}

%find_lang %{name} --with-man --all-name --generate-subpackages

%files
%license COPYING.txt
%doc ChangeLog.txt NEWS.txt README.txt TODO.txt
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%{_bindir}/unix2dos
%{_bindir}/unix2mac
%{_mandir}/man1/*.1*

%changelog
%autochangelog
