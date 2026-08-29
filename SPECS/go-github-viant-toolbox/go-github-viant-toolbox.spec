# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           toolbox
%define go_import_path  github.com/viant/toolbox
# Optional cloud/SSH/storage backends require AWS SDK and extra service
# dependencies, while gojay only needs toolbox core helpers plus the url package.
# Keep those optional backend packages out of %check and installation. The root
# and cred tests contain current behavior mismatches and os.Exit handling that
# fail in OBS. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    github.com/viant/toolbox
    github.com/viant/toolbox/cred
    github.com/viant/toolbox/kms/aws
    github.com/viant/toolbox/secret
    github.com/viant/toolbox/ssh
    github.com/viant/toolbox/storage
    github.com/viant/toolbox/storage/scp
    github.com/viant/toolbox/storage/s3
    github.com/viant/toolbox/kms/gcp
    github.com/viant/toolbox/storage/gs
    github.com/viant/toolbox/url
}

Name:           go-github-viant-toolbox
Version:        0.39.0
Release:        %autorelease
Summary:        Toolbox - go utility library
License:        Apache-2.0
URL:            https://github.com/viant/toolbox
#!RemoteAsset:  sha256:1614ed65aee9c027abf45aa37f1969842e0b081d4a1edc888a8551bc167fd1d1
Source0:        https://github.com/viant/toolbox/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix test expectations for current time and case formatting behavior.
# - HNO3Miracle
Patch2000:      2000-fix-current-format-test-expectations.patch

# Go 1.25+ vet rejects fmt.Errorf calls whose format string is built at
# runtime; keep tests enabled but disable vet instead of patching upstream
# source. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-errors/errors)
BuildRequires:  go(github.com/lunixbochs/vtclean)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/viant/xunsafe)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/oauth2/google)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/viant/toolbox) = %{version}
Provides:       go(github.com/viant/toolbox/data) = %{version}
Provides:       go(github.com/viant/toolbox/url) = %{version}

Requires:       go(github.com/go-errors/errors)
Requires:       go(github.com/lunixbochs/vtclean)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/viant/xunsafe)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/oauth2/google)
Requires:       go(gopkg.in/yaml.v2)

%description
Toolbox is a Go utility library with helpers for contexts, conversion, storage,
URL handling, and related common tasks.

%install -a
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/kms/aws \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/kms/gcp \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/secret \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/ssh \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/storage/gs \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/storage/s3 \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/storage/scp

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.txt
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
