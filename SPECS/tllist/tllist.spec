# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tllist
Version:        1.1.0
Release:        %autorelease
Summary:        C header file only implementation of a typed linked list
License:        MIT
URL:            https://codeberg.org/dnkl/tllist
#!RemoteAsset:  sha256:a1f0ce0dc4fcb4ce59c37202a1d914c853a8bd2d7c5d57d623b15a8dd9778767
Source0:        https://codeberg.org/dnkl/tllist/releases/download/%{version}/tllist-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc

%description
tllist is a C header-only implementation of a linked list that uses
pre-processor macros to implement dynamic types.

%package        devel
Summary:        Development files for %{name}

%description    devel
Development files for tllist.

%files devel
%{_includedir}/tllist.h
%{_libdir}/pkgconfig/tllist.pc
%{_docdir}/tllist

%changelog
%autochangelog
