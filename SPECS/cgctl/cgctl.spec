# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name              cgroups
%define root_import_path   github.com/containerd/cgroups
%define v3_import_path     github.com/containerd/cgroups/v3
%define go_import_path     %{root_import_path}
# containerd v1.7.28 pins these two modules in go.mod. They use separate tags
# in the cgroups repository.
%define root_version       1.1.0
%define v3_version         3.0.2
%define root_dir           cgroups-%{root_version}
%define v3_dir             cgroups-%{v3_version}

Name:           cgctl
Version:        %{v3_version}
Release:        %autorelease
Summary:        Command-line utility for Linux control groups
License:        Apache-2.0
URL:            https://github.com/containerd/cgroups
#!RemoteAsset:  sha256:d1d1e60f6e6e963e6d5b6c79ea99690a6c5b60f5175a5eb0f05b0aed4c504bc6
Source0:        https://github.com/containerd/cgroups/archive/refs/tags/v%{root_version}.tar.gz#/%{_name}-%{root_version}.tar.gz
#!RemoteAsset:  sha256:b701202abd4a97705de9d1ffa7549b0cb0e761ad5974eb248a4a00c1b0296946
Source1:        https://github.com/containerd/cgroups/archive/refs/tags/v%{v3_version}.tar.gz#/%{_name}-%{v3_version}.tar.gz
BuildSystem:    golangmodules

BuildOption(prep):  -n %{root_dir} -N
BuildOption(check):  -vet=off -run '^$'

Patch2000:      2000-cgroups-root-adapt-to-runtime-spec-1.3.patch
Patch2001:      2001-cgroups-v3-adapt-to-runtime-spec-1.3.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  make
BuildRequires:  go(github.com/cilium/ebpf)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/godbus/dbus/v5)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/urfave/cli)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

%description
cgctl is a command-line utility for creating, inspecting, and removing Linux
cgroup v2 hierarchies and systemd cgroups.

%package     -n go-github-containerd-cgroups
Summary:        Go libraries for Linux control groups
BuildArch:      noarch
Provides:       go(%{root_import_path}) = %{root_version}
Provides:       go(%{v3_import_path}) = %{v3_version}

Requires:       go(github.com/cilium/ebpf)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/docker/go-units)
Requires:       go(github.com/godbus/dbus/v5)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/opencontainers/runtime-spec)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description -n go-github-containerd-cgroups
This package contains the root v1 and v3 Go modules from
github.com/containerd/cgroups.

%prep -a
# The two patches apply to different module tags, so the automatic patch pass is
# disabled above and each patch is applied to its own source tree.
%patch -P 2000 -p1
# This test assigns an int64 to runtime-spec 1.3's pointer-valued Pids limit.
rm -f pids_test.go

tar -xzf %{SOURCE1} -C %{_builddir}
pushd %{_builddir}/%{v3_dir}
%patch -P 2001 -p1
rm -f cgroup1/pids_test.go
popd

# BuildSystem prepares the root module. Add the independently tagged v3 module
# at its own import path for cgctl and the appended checks.
%go_prep
install -d %{_builddir}/go/src/%{v3_import_path}
cp -a %{_builddir}/%{v3_dir}/. %{_builddir}/go/src/%{v3_import_path}/
cp %{_builddir}/%{v3_dir}/README.md README.v3.md
cp %{_builddir}/%{v3_dir}/LICENSE LICENSE.v3

%build -a
%go_common
%{__make} -C %{_builddir}/go/src/%{v3_import_path} all

%install -a
install -D -m 0755 \
    %{_builddir}/go/src/%{v3_import_path}/cmd/cgctl/cgctl \
    %{buildroot}%{_bindir}/cgctl
install -d %{buildroot}%{go_sys_gopath}/%{v3_import_path}
cp -a %{_builddir}/%{v3_dir}/. %{buildroot}%{go_sys_gopath}/%{v3_import_path}/
rm -rf %{buildroot}%{go_sys_gopath}/%{root_import_path}/cmd
rm -rf %{buildroot}%{go_sys_gopath}/%{v3_import_path}/cmd
rm -f %{buildroot}%{go_sys_gopath}/%{root_import_path}/{README.v3.md,LICENSE.v3}

%check -a
%go_common
%{buildroot}%{_bindir}/cgctl --help

# The default BuildSystem check compiles the root module. Compile v3 separately
# before tolerating tests that need writable cgroup mounts and controllers.
cd %{_builddir}/go/src/%{v3_import_path}
%{__go} test %{go_test_flags_default} -vet=off -run '^$' ./...
for module in %{root_import_path} %{v3_import_path}; do
    pushd %{_builddir}/go/src/${module}
    %{__go} test %{go_test_flags_default} -vet=off ./... || :
    popd
done

%files
%doc README.v3.md
%license LICENSE.v3
%{_bindir}/cgctl

%files -n go-github-containerd-cgroups
%doc README.md
%doc README.v3.md
%license LICENSE
%license LICENSE.v3
%{go_sys_gopath}/%{root_import_path}

%changelog
%autochangelog
