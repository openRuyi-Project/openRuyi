# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sed
Version:        4.9
Release:        %autorelease
Summary:        A Stream-Oriented Non-Interactive Text Editor
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/sed/
VCS:            git:https://https.git.savannah.gnu.org/git/sed.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/sed/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/sed/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --without-included-regex

BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libselinux)

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
