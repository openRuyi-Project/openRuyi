# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-multierror
%define go_import_path  github.com/hashicorp/go-multierror

Name:           go-github-hashicorp-go-multierror
Version:        1.1.1
Release:        %autorelease
Summary:        A Go (golang) package for representing a list of errors as a single error.
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-multierror
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-multierror/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/errwrap)

Provides:       go(github.com/hashicorp/go-multierror) = %{version}

%description
go-multierror is a package for Go that provides a mechanism for
representing a list of error values as a single error.

This allows a function in Go to return an error that might actually be a
list of errors. If the caller knows this, they can unwrap the list and
access the errors. If the caller doesn't know, the error formats to a
nice human-readable format.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
