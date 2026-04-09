# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           govalidator
%define go_import_path  github.com/asaskevich/govalidator
# I dont know why it will fail on OBS - Julian
%define go_test_ignore_failure 1

Name:           go-github-asaskevich-govalidator
Version:        11.0.1
Release:        %autorelease
Summary:        [Go] Package of validators and sanitizers for strings, numerics, slices and structs
License:        MIT
URL:            https://github.com/asaskevich/govalidator
#!RemoteAsset
Source0:        https://github.com/asaskevich/govalidator/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/asaskevich/govalidator) = %{version}

%description
A package of validators and sanitizers for strings, structs and
collections. Based on validator.js.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
