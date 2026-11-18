# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libpathrs
%define go_import_path  cyphar.com/go-pathrs

Name:           go-github-cyphar-libpathrs
Version:        0.2.6
Release:        %autorelease
Summary:        Go bindings and support sources for safe Linux path resolution
License:        MPL-2.0 AND Apache-2.0 AND CC0-1.0
URL:            https://github.com/cyphar/libpathrs
#!RemoteAsset:  sha256:6aac480634e9b1dd8a74db4022dbb2ae70208fe5335f4d25345513ac53dbf3e9
Source0:        https://github.com/cyphar/libpathrs/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Supply the missing mode argument without disabling vet for the e2e command.
# https://github.com/cyphar/libpathrs/commit/0f150c3d23853ed5a74b8883838f1b60f1178ce3
Patch1000:      1000-fix-mode-error-format-argument.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  gcc
BuildRequires:  go >= 1.24
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(pathrs) >= %{version}
BuildRequires:  go(github.com/urfave/cli/v3)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/internal/fdutils) = %{version}
Provides:       go(%{go_import_path}/internal/libpathrs) = %{version}
Provides:       go(%{go_import_path}/procfs) = %{version}

Requires:       pkgconfig(pathrs) >= %{version}
Requires:       go(github.com/urfave/cli/v3)
Requires:       go(golang.org/x/sys)

%description
Go bindings for libpathrs provide safe path resolution and procfs access on
Linux. This package retains the complete upstream source snapshot, including
the example and end-to-end command modules, and uses the system libpathrs.

%install
# Preserve the complete repository and move all three Go modules to their
# declared import paths; the VCS root itself is not a Go module.
install -d %{buildroot}%{go_sys_gopath}/github.com/cyphar/%{_name}
cp -a . %{buildroot}%{go_sys_gopath}/github.com/cyphar/%{_name}/
install -d %{buildroot}%{go_sys_gopath}/cyphar.com
mv %{buildroot}%{go_sys_gopath}/github.com/cyphar/%{_name}/go-pathrs %{buildroot}%{go_sys_gopath}/%{go_import_path}
mv %{buildroot}%{go_sys_gopath}/github.com/cyphar/%{_name}/examples/go %{buildroot}%{go_sys_gopath}/pathrs-example
mv %{buildroot}%{go_sys_gopath}/github.com/cyphar/%{_name}/e2e-tests/cmd/go %{buildroot}%{go_sys_gopath}/pathrs-cmd
# These upstream links cross the relocated module boundary.
ln -sfn ../../github.com/cyphar/%{_name}/include/pathrs.h %{buildroot}%{go_sys_gopath}/%{go_import_path}/pathrs.h
ln -sfn ../../../../../%{go_import_path} %{buildroot}%{go_sys_gopath}/github.com/cyphar/%{_name}/contrib/bindings/go

%check
# Use the installed module layout in GOPATH mode, including the e2e command.
# Each example defines its own main, so compile and vet each file separately,
# as upstream's examples/go/Makefile does, rather than combining the programs.
%go_common
export CGO_ENABLED=1
export GOPATH="%{buildroot}%{go_sys_gopath}/..:${GOPATH}"
%__go test %{go_test_flags_default} %{go_import_path}/... pathrs-cmd/...
for example in %{buildroot}%{go_sys_gopath}/pathrs-example/*.go; do
    %__go test %{go_test_flags_default} "$example"
done

%files
%doc README.md CHANGELOG.md INSTALL.md
%license COPYING.md LICENSE.MPL-2.0 LICENSE.LGPL-3.0 LICENSE.GPL-3.0
%license go-pathrs/COPYING
%license hack/keyring-addkey.sh hack/keyring-validate.sh hack/readlinkf.sh
%{go_sys_gopath}/github.com/cyphar/%{_name}
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/pathrs-example
%{go_sys_gopath}/pathrs-cmd

%changelog
%autochangelog
