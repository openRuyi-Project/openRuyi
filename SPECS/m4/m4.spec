# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Define build conditionals for optional features
%bcond nls 0

%if %{without nls}
%global build_cflags %{build_cflags} -Wno-format-security
%endif

Name:           m4
Version:        1.4.21
Release:        %autorelease
Summary:        The GNU macro processor
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/m4/
VCS:            git:http://git.savannah.gnu.org/r/m4.git
#!RemoteAsset:  sha256:f25c6ab51548a73a75558742fb031e0625d6485fe5f9155949d6486a2408ab66
Source0:        https://ftpmirror.gnu.org/gnu/m4/m4-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --without-included-regex
%if %{with nls}
BuildOption(conf):  --enable-nls
%else
BuildOption(conf):  --disable-nls
%endif

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
%if %{with nls}
BuildRequires:  gettext
%endif

%description
A GNU implementation of the traditional UNIX macro processor. M4 is
useful for writing text files which can be logically parsed, and is used
by many programs, such as autoconf, as part of their build process.

%if %{with nls}
%install -a
rm -f %{buildroot}%{_infodir}/dir

%find_lang %{name} --generate-subpackages
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/m4
%{_mandir}/man1/m4.1*
%{_infodir}/m4.info*

%changelog
%{?autochangelog}
