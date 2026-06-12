# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond acl 1
%bcond selinux 1

Name:           sed
Version:        4.9
Release:        %autorelease
Summary:        A Stream-Oriented Non-Interactive Text Editor
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/sed/
VCS:            git:https://https.git.savannah.gnu.org/git/sed.git
#!RemoteAsset:  sha256:6e226b732e1cd739464ad6862bd1a1aba42d7982922da7a53519631d24975181
Source0:        https://ftpmirror.gnu.org/gnu/sed/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --without-included-regex
%if %{without acl}
BuildOption(conf):  --disable-acl
%endif
%if %{without selinux}
BuildOption(conf):  --without-selinux
%endif

%if %{with acl}
BuildRequires:  pkgconfig(libacl)
%endif
%if %{with selinux}
BuildRequires:  pkgconfig(libselinux)
%endif

Provides:       base:/bin/sed

%description
Sed takes text input, performs one or more operations on it, and
outputs the modified text. Sed is typically used for extracting parts
of a file using pattern matching or  for substituting multiple
occurrences of a string within a file.

%install -a
%find_lang %{name} --generate-subpackages

%files
%license COPYING*
%doc AUTHORS BUGS NEWS README* THANKS
%{_bindir}/sed
%{_mandir}/man*/*%{ext_man}
%{_infodir}/sed.info*%{ext_info}

%changelog
%autochangelog
