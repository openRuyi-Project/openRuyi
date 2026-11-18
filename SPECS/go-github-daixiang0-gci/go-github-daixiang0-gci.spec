# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gci
%define go_import_path  github.com/daixiang0/gci

Name:           go-github-daixiang0-gci
Version:        0.14.0
Release:        %autorelease
Summary:        Go import ordering and formatting library
License:        BSD-3-Clause
URL:            https://github.com/daixiang0/gci
#!RemoteAsset:  sha256:433d6dd89ebcb9f928f91729b9243971f6233970f78efc41ae672fe376de4e88
Source0:        https://github.com/daixiang0/gci/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.24.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/hexops/gotextdiff)
BuildRequires:  go(github.com/hexops/gotextdiff/myers)
BuildRequires:  go(github.com/hexops/gotextdiff/span)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/zap/zapcore)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/mod/modfile)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/errgroup)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/ast/astutil)
BuildRequires:  go(golang.org/x/tools/go/packages)
BuildRequires:  go(gopkg.in/yaml.v3)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/daixiang0/gci) = %{version}
Provides:       go(github.com/daixiang0/gci/cmd/gci) = %{version}
Provides:       go(github.com/daixiang0/gci/internal) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/config) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/format) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/gci) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/io) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/log) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/parse) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/section) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/specificity) = %{version}
Provides:       go(github.com/daixiang0/gci/pkg/utils) = %{version}
Provides:       go(github.com/daixiang0/gci/v2) = %{version}
Provides:       go(github.com/daixiang0/gci/v2/cmd/gci) = %{version}
Provides:       go(github.com/daixiang0/gci/v2/internal/imports) = %{version}
Provides:       go(github.com/daixiang0/gci/v2/pkg/config) = %{version}
Provides:       go(github.com/daixiang0/gci/v2/pkg/gci) = %{version}
Provides:       go(github.com/daixiang0/gci/v2/pkg/parse) = %{version}
Provides:       go(github.com/daixiang0/gci/v2/pkg/section) = %{version}
Provides:       go(github.com/daixiang0/gci/v2/pkg/specificity) = %{version}

Requires:       go(github.com/hexops/gotextdiff)
Requires:       go(github.com/hexops/gotextdiff/myers)
Requires:       go(github.com/hexops/gotextdiff/span)
Requires:       go(github.com/spf13/cobra)
Requires:       go(go.uber.org/zap)
Requires:       go(go.uber.org/zap/zapcore)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/mod/modfile)
Requires:       go(golang.org/x/sync/errgroup)
Requires:       go(golang.org/x/tools/go/ast/astutil)
Requires:       go(golang.org/x/tools/go/packages)
Requires:       go(gopkg.in/yaml.v3)

%description
Go import ordering and formatting library. This package contains the complete
upstream repository sources and tests.

# Exercise every non-fixture nested module as well as the root module.
%check -a
%go_common
pushd %{_builddir}/go/src/github.com/daixiang0/gci/v2
%{__go} test %{go_test_flags_default} ./...
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
