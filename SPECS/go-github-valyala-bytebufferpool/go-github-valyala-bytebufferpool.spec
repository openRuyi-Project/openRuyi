# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bytebufferpool
%define go_import_path  github.com/valyala/bytebufferpool

Name:           go-github-valyala-bytebufferpool
Version:        1.0.0
Release:        %autorelease
Summary:        Anti-memory-waste byte buffer pool
License:        MIT
URL:            https://github.com/valyala/bytebufferpool
#!RemoteAsset
Source0:        https://github.com/valyala/bytebufferpool/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/valyala/bytebufferpool) = %{version}

%description
An implementation of a pool of byte buffers with
anti-memory-waste protection.

The pool may waste limited amount of memory due to
fragmentation. This amount equals to the maximum
total size of the byte buffers in concurrent use.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
