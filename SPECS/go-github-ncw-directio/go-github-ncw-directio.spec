# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           directio
%define go_import_path  github.com/ncw/directio

Name:           go-github-ncw-directio
Version:        1.0.4
Release:        %autorelease
Summary:        This is library for the Go language to enable use of Direct IO under all OSes
License:        MIT
URL:            https://github.com/ncw/directio
#!RemoteAsset
Source0:        https://github.com/ncw/directio/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/ncw/directio) = %{version}

%description
This is library for the Go language to enable use of Direct IO under all
supported OSes of Go (except openbsd and plan9).

Direct IO does IO to and from disk without buffering data in the OS. It
is useful when you are reading or writing lots of data you don't want to
fill the OS cache up with.

%files
%license COPYING*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
