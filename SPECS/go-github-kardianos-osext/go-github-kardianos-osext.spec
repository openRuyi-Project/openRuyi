# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           osext
%define go_import_path  github.com/kardianos/osext
%define commit_id       2bc1f35cddc0cc527b4bc3dce8578fc2a6c11384

Name:           go-github-kardianos-osext
Version:        0+git20260621.2bc1f35
Release:        %autorelease
Summary:        Extensions to the standard "os" package. Executable and ExecutableFolder.
License:        BSD-3-Clause
URL:            https://github.com/kardianos/osext
#!RemoteAsset:  sha256:2d4c4a4bbfdc3a34e50224f7b30ea4907a5e459e7940c03e34a9b7a13e07f841
Source0:        https://github.com/kardianos/osext/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kardianos/osext) = %{version}

%description
osext provides helpers to find the path and directory of the running executable.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
