# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonschema
%define go_import_path  github.com/karimkhaleel/jsonschema
%define commit_id       d933f0d94ea32bb3694350beaa2bd7e7cdc27121

Name:           go-github-karimkhaleel-jsonschema
Version:        0+git20260621.d933f0d
Release:        %autorelease
Summary:        Generate JSON Schemas from Go types
License:        MIT
URL:            https://github.com/karimkhaleel/jsonschema
#!RemoteAsset:  sha256:db14ca5d6fbddd5f6c6536195bbda13b6c2ca0f36faf27ddfaf76339edc905d1
Source0:        https://github.com/karimkhaleel/jsonschema/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/wk8/go-ordered-map/v2)

Provides:       go(github.com/karimkhaleel/jsonschema) = %{version}

Requires:       go(github.com/wk8/go-ordered-map/v2)

%description
jsonschema generates JSON Schema documents from Go types via reflection.

# This fork retained tests and examples that import its upstream module path,
# github.com/invopop/jsonschema, instead of testing the packaged fork. Remove
# those stale files while retaining compilation of the library used by lazygit.
%prep -a
rm -rf examples
rm -f id_test.go examples_test.go reflect_test.go

%files
%doc README*
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
