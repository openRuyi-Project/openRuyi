# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gordf
%define go_import_path  github.com/spdx/gordf
%define commit_id       7098f93598fb

Name:           go-github-spdx-gordf
Version:        0+git20260718.7098f93
Release:        %autorelease
Summary:        gordf is a package which provides a parser for RDF files linearized using RDF/XML format.
License:        MIT
URL:            https://github.com/spdx/gordf
#!RemoteAsset:  sha256:1fd11626c57a3d1d8f98f88b84bb636d77f3cf5859f3178a0e05045a7e564a34
Source0:        %{url}/archive/7098f93598fb.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
# Current Go vet rejects upstream tests that pass non-constant strings to Errorf.
# Keep the test suite running while disabling vet-only failures. - Jvle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/spdx/gordf) = %{version}

%description
gordf is a package which provides a parser for RDF files linearized
using RDF/XML format. It will be used to represent the rdf files in
memory and write back in possibly different formats like json, and xml.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
