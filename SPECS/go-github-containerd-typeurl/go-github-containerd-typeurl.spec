# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           typeurl
%define go_import_path  github.com/containerd/typeurl

Name:           go-github-containerd-typeurl
Version:        2.2.2
Release:        %autorelease
Summary:        Go package for managing marshaled types to protobuf.Any
License:        Apache-2.0
URL:            https://github.com/containerd/typeurl
#!RemoteAsset
Source0:        https://github.com/containerd/typeurl/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(github.com/gogo/protobuf)

Provides:       go(github.com/containerd/typeurl) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
A Go package for managing the registration, marshaling, and unmarshaling
of encoded types.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
