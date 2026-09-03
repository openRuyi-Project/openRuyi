# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-yaml
%define go_import_path  github.com/itchyny/go-yaml
# The YAML Test Suite data is downloaded separately and is not in the archive.
%define go_test_exclude %{go_import_path}/yts
%define commit_id       fca9a0999f15f0617aa2e3d926f187d9bc8bfd0a

Name:           go-github-itchyny-go-yaml
Version:        0+git20260819.fca9a09
Release:        %autorelease
Summary:        YAML support for the Go language
License:        Apache-2.0 AND MIT
URL:            https://github.com/itchyny/go-yaml
#!RemoteAsset:  sha256:47aec9eefee13226d9015a2f417521dbcf6aed6e64a10e7446bc858de9c57daf
Source0:        https://github.com/itchyny/go-yaml/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This compatibility module provides YAML encoding and decoding under the former
github.com/itchyny/go-yaml import path used by existing consumers.

%check -a
# Compile yts without running tests because the YAML Test Suite data is not
# included in the source archive.
%__go test -run '^$' %{go_import_path}/yts

%files
%doc README.md NOTICE
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
