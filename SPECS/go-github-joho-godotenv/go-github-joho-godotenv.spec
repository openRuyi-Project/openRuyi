# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           godotenv
%define go_import_path  github.com/joho/godotenv

Name:           go-github-joho-godotenv
Version:        1.5.1
Release:        %autorelease
Summary:        Dotenv file loader for Go
License:        MIT
URL:            https://github.com/joho/godotenv
#!RemoteAsset:  sha256:f87c261109efd54c8f16b40252e820d690af571975c25247d2438c43be0be4a1
Source0:        https://github.com/joho/godotenv/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package loads environment variables from dotenv files in Go programs.

%files
%doc README.md
%license LICENCE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
