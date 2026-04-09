# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errwrap
%define go_import_path  github.com/hashicorp/errwrap

Name:           go-github-hashicorp-errwrap
Version:        1.1.0
Release:        %autorelease
Summary:        Errwrap is a Go (golang) library for wrapping and querying errors.
License:        MPL-2.0
URL:            https://github.com/hashicorp/errwrap
#!RemoteAsset
Source0:        https://github.com/hashicorp/errwrap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/errwrap) = %{version}

%description
errwrap is a package for Go that formalizes the pattern of wrapping
errors and checking if an error contains another error.

There is a common pattern in Go of taking a returned error value and
then wrapping it (such as with fmt.Errorf) before returning it. The
problem with this pattern is that you completely lose the original error
structure.

Arguably the *correct* approach is that you should make a custom
structure implementing the error interface, and have the original error
as a field on that structure, such as this example
(http://golang.org/pkg/os/#PathError). This is a good approach, but you
have to know the entire chain of possible rewrapping that happens, when
you might just care about one.

errwrap formalizes this pattern (it doesn't matter what approach you use
above) by giving a single interface for wrapping errors, checking if a
specific error is wrapped, and extracting that error.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
