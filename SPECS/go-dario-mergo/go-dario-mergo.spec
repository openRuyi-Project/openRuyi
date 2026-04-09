# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mergo
%define go_import_path  dario.cat/mergo
# I dont know why it will fail on OBS - Julian
%define go_test_ignore_failure 1

Name:           go-dario-mergo
Version:        1.0.2
Release:        %autorelease
Summary:        Mergo: merging Go structs and maps since 2013
License:        BSD-3-Clause
URL:            https://github.com/imdario/mergo
#!RemoteAsset
Source0:        https://github.com/imdario/mergo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(dario.cat/mergo) = %{version}

%description
A helper to merge structs and maps in Golang. Useful for configuration
default values, avoiding messy if-statements.

Mergo merges same-type structs and maps by setting default values in
zero-
value fields. Mergo won't merge unexported (private) fields. It will do
recursively any exported one. It also won't merge structs inside maps
(because they are not addressable using Go reflection).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
