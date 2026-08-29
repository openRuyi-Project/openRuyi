# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tar2go
%define go_import_path  github.com/cpuguy83/tar2go

Name:           go-github-cpuguy83-tar2go
Version:        0.3.1
Release:        %autorelease
Summary:        Expose a tar archive as a Go io/fs filesystem
License:        MIT
URL:            https://github.com/cpuguy83/tar2go
#!RemoteAsset:  sha256:9088bf2ab0459fb981086a1c5024764b7840277f1bbec7b7faf379abe70ca793
Source0:        https://github.com/cpuguy83/tar2go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cpuguy83/tar2go) = %{version}

%description
tar2go exposes the contents of a tar archive through the Go io/fs.FS interface.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
