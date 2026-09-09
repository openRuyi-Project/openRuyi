# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mongo-driver
%define go_import_path  go.mongodb.org/mongo-driver

Name:           go-mongodb-mongo-driver
Version:        1.17.3
Release:        %autorelease
Summary:        MongoDB Go driver v1
License:        Apache-2.0
URL:            https://github.com/mongodb/mongo-go-driver
#!RemoteAsset:  sha256:afc937f54185a2dd7bf5e9db7928dfc716310279726bea3a69dfcbc341ecdc35
Source0:        https://github.com/mongodb/mongo-go-driver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep existing test diagnostics compatible with Go vet.
Patch2000:      2000-fix-test-format-strings.patch
# Honor upstream short mode for tests requiring external DNS or MongoDB.
Patch2001:      2001-honor-short-mode-for-external-tests.patch

# Upstream short mode runs unit tests without a live MongoDB deployment.
BuildOption(check):  -short -timeout 15m

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/montanaflynn/stats)
BuildRequires:  go(github.com/xdg-go/scram)
BuildRequires:  go(github.com/xdg-go/stringprep)
BuildRequires:  go(github.com/youmark/pkcs8)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sync)

Provides:       go(go.mongodb.org/mongo-driver) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/golang/snappy)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/montanaflynn/stats)
Requires:       go(github.com/xdg-go/scram)
Requires:       go(github.com/xdg-go/stringprep)
Requires:       go(github.com/youmark/pkcs8)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sync)

%description
The MongoDB Go driver provides BSON encoding, database operations,
authentication, connection pooling, and monitoring for Go applications.
This package supplies the v1 import path used by MinIO.

%prep -a
# Build against distribution Go packages rather than the upstream vendor copy.
rm -rf vendor
# These separate Go modules are live AWS Lambda and MongoDB leak-test harnesses.
# Module-mode root tests omit them; do not pull them into the GOPATH build.
rm -rf internal/test/faas/awslambda/mongodb internal/test/goleak

%check -p
# The BSON local-time test requires a local zone distinct from UTC.
export TZ=America/New_York

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
