# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond manpages 1

Name:           autoconf
Version:        2.72
Release:        %autorelease
Summary:        A GNU Tool for Automatically Configuring Source Code
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/autoconf
VCS:            git:https://git.savannah.gnu.org/git/autoconf.git
#!RemoteAsset:  sha256:ba885c1319578d6c94d46e9b0dceb4014caafe2490e437a0dbca3f270a223f5a
Source0:        https://ftpmirror.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    autotools

Patch0:         autoreconf-ltdl.diff

%if %{with manpages}
BuildRequires:  help2man
%endif
BuildRequires:  m4 >= 1.4.16
BuildRequires:  perl >= 5.10

Requires:       m4 >= 1.4.16
Requires:       perl >= 5.10

%description
GNU Autoconf is a tool for configuring source code and makefiles. Using
autoconf, programmers can create portable and configurable packages,
because the person building the package is allowed to specify various
configuration options.

You should install autoconf if you are developing software and would
like to create shell scripts to configure your source code packages.

Note that the autoconf package is not required for the end user who may
be configuring software with an autoconf-generated script; autoconf is
only required for the generation of the scripts, not their use.

%build -p
%if %{without manpages}
# Release tarballs already carry these generated pages.
touch man/*.1
%endif

%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_bindir}/*
%{_datadir}/autoconf
%{_infodir}/*.gz
%{_mandir}/man1/*.gz

%changelog
%autochangelog
