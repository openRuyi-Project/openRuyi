# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hashstructure
%define go_import_path  github.com/mitchellh/hashstructure

Name:           go-github-mitchellh-hashstructure
Version:        2.0.2
Release:        %autorelease
Summary:        Get hash values for arbitrary values in Go (golang).
License:        MIT
URL:            https://github.com/mitchellh/hashstructure
#!RemoteAsset
Source0:        https://github.com/mitchellh/hashstructure/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mitchellh/hashstructure) = %{version}

%description
hashstructure is a Go library for creating a unique hash value for
arbitrary values in Go.

This can be used to key values in a hash (for use in a map, set, etc.)
that are complex. The most common use case is comparing two values
without sending data across the network, caching values locally (de-dup),
and so on.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
