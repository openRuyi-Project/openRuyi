# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-gatedio
%define go_import_path  github.com/hashicorp/go-gatedio

Name:           go-github-hashicorp-go-gatedio
Version:        0.5.0
Release:        %autorelease
Summary:        Provides a unified interface for wrapping io objects in a mutex
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-gatedio
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-gatedio/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-gatedio) = %{version}

%description
The gatedio package provides tiny wrappers around the io.ReadWriter,
io.Writer, and io.Reader interfaces to support concurrent usage and
access across multiple goroutines.

This library is especially useful in tests where a bytes.Buffer may be
used. Go's native bytes.Buffer is not safe across multiple goroutes and
therefore must be wrapped in some kind of mutex.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
