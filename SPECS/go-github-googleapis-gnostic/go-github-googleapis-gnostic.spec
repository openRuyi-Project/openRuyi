# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gnostic
%define go_import_path  github.com/googleapis/gnostic

Name:           go-github-googleapis-gnostic
Version:        0.4.1
Release:        %autorelease
Summary:        OpenAPI and discovery models and parsers for Go
License:        Apache-2.0
URL:            https://github.com/googleapis/gnostic
#!RemoteAsset:  sha256:cc20ab94cf800fdfe377778aa0e2c640045c80193a873253e97605297801733f
Source0:        https://github.com/googleapis/gnostic/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 rejects the legacy plugin logging format under vet.
BuildOption(check):  -vet=off
# Remote fixtures need network; the extension example needs plugins absent from the archive.
BuildOption(check):  -skip '^(TestRemote(Petstore|Separate)(JSON|YAML)|TestExtensionHandlerWithLibraryExample)$'

BuildRequires:  diffutils
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/docopt/docopt-go)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/googleapis/gnostic) = %{version}

Requires:       go(github.com/docopt/docopt-go)
Requires:       go(github.com/golang/protobuf)
Requires:       go(gopkg.in/yaml.v2)

%description
Gnostic provides OpenAPI and discovery models backed by Protocol Buffers,
with parsers and utilities for processing API descriptions in Go.

# Upstream tests execute the compiler and bundled plugins.
%check -p
%{go_common}
%{go_prep}
export PATH="%{_builddir}/go/bin:$PATH"
go install %{go_import_path}/...
# The generator treats GOPATH as one directory; give only this test tool a single root.
mkdir -p %{_builddir}/test-tools
cat > %{_builddir}/test-tools/generate-gnostic <<'EOF'
#!/bin/sh
GOPATH="%{_builddir}/go" exec "%{_builddir}/go/bin/generate-gnostic" "$@"
EOF
chmod +x %{_builddir}/test-tools/generate-gnostic
export PATH="%{_builddir}/test-tools:$PATH"

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
