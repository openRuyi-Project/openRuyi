# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pdf
%define go_import_path  github.com/ledongthuc/pdf
%define commit_id       5959a40277285327ee480a3bfd8ec9289fc1ab50
# pdfpasswd retains the canonical rsc.io/pdf/pdfpasswd import comment.
%define go_test_exclude %{go_import_path}/pdfpasswd

Name:           go-github-ledongthuc-pdf
Version:        0+git20250511.5959a40
Release:        %autorelease
Summary:        Go library for reading PDF files
License:        BSD-3-Clause
URL:            https://github.com/ledongthuc/pdf
#!RemoteAsset:  sha256:bf9db7bc693f66de5d9f427b0a42b728ff8b0f8771804debf1cd87c25e4ac0cd
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides a Go library for extracting text and formatting
information from PDF files.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
