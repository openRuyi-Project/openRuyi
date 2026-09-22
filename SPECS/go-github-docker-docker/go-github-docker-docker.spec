# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           docker
%define go_import_path  github.com/docker/docker
%define go_test_include %{shrink:
    %{go_import_path}/api/types
    %{go_import_path}/api/types/blkiodev
    %{go_import_path}/api/types/container
    %{go_import_path}/api/types/filters
    %{go_import_path}/api/types/mount
    %{go_import_path}/api/types/network
    %{go_import_path}/api/types/registry
    %{go_import_path}/api/types/strslice
    %{go_import_path}/api/types/swarm
    %{go_import_path}/api/types/swarm/runtime
    %{go_import_path}/api/types/versions
    %{go_import_path}/errdefs
    %{go_import_path}/pkg/homedir
    %{go_import_path}/pkg/idtools
    %{go_import_path}/pkg/ioutils
    %{go_import_path}/pkg/jsonmessage
    %{go_import_path}/pkg/mount
    %{go_import_path}/pkg/stringid
    %{go_import_path}/pkg/system
    %{go_import_path}/pkg/tarsum
    %{go_import_path}/pkg/term
    %{go_import_path}/registry
    %{go_import_path}/registry/resumable
    %{go_import_path}/rootless
}

Name:           go-github-docker-docker
Version:        17.12.0~ce~rc1+git20200916.bd33bbf
Release:        %autorelease
Summary:        Go library for docker
License:        Apache-2.0
URL:            https://github.com/docker/docker
VCS:            git:https://github.com/docker/docker.git
#!RemoteAsset:  sha256:5b9dbd3096a19cf4670337ead2120fdd38296fcb752ae2f5fffbf5547d26d9ed
Source0:        https://github.com/docker/docker/archive/bd33bbf0497b.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# docker/go-connections 0.8 removed DialerFromEnvironment. The transport
# already uses http.ProxyFromEnvironment, so retain its direct net.Dialer.
Patch0:         0001-registry-use-net-dialer-directly.patch

BuildOption(prep):  -n moby-bd33bbf0497b2327516dc799a5e541b720822a4c
# Validate exactly the packages imported by Cloudpods. The full Moby tree also
# contains daemon and integration packages that require privileged services.
BuildOption(check):  -vet=off -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/containerd)
BuildRequires:  go(github.com/containerd/continuity)
BuildRequires:  go(github.com/docker/distribution)
BuildRequires:  go(github.com/docker/go-connections)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/morikuni/aec)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/opencontainers/runc)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(gotest.tools/assert)

Provides:       go(github.com/docker/docker) = %{version}

Requires:       go(github.com/containerd/containerd)
Requires:       go(github.com/containerd/continuity)
Requires:       go(github.com/docker/distribution)
Requires:       go(github.com/docker/go-connections)
Requires:       go(github.com/docker/go-units)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/morikuni/aec)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/opencontainers/runc)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/grpc)

%description
This package provides the github.com/docker/docker Go module source.

%prep -a
# Do not install a nested vendor tree into the shared Go source path.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
