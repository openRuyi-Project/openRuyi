# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           moby-sys
%define go_import_path  github.com/moby/sys

%define ver_atomicwriter 0.1.0
%define ver_sequential   0.7.0
%define ver_mountinfo    0.6.2
%define ver_signal       0.7.0
%define ver_user         0.3.0
%define ver_userns       0.1.0

%define dir_atomicwriter sys-atomicwriter-v%{ver_atomicwriter}
%define dir_sequential   sys-sequential-v%{ver_sequential}
%define dir_mountinfo    sys-mountinfo-v%{ver_mountinfo}
%define dir_signal       sys-signal-v%{ver_signal}
%define dir_user         sys-user-v%{ver_user}
%define dir_userns       sys-userns-v%{ver_userns}

# The package version is the date of the newest selected module tag,
# sequential/v0.7.0. Each module keeps its real version in Provides.
Name:           go-github-moby-sys
Version:        20260605
Release:        %autorelease
Summary:        Go system utility modules from Moby
License:        Apache-2.0
URL:            https://github.com/moby/sys
BuildArch:      noarch
BuildSystem:    golangmodules

#!RemoteAsset:  sha256:c0cfe5c26d24ba36cfbdeca9b993563273ca5ba0692140bc0d3f1a75e8c336c1
Source0:        https://github.com/moby/sys/archive/refs/tags/atomicwriter/v%{ver_atomicwriter}.tar.gz#/%{_name}-atomicwriter-%{ver_atomicwriter}.tar.gz
#!RemoteAsset:  sha256:87fa39a6874627d7cea81c837bf2e5caf25b7a4bc4f0ea18057223cc85771393
Source1:        https://github.com/moby/sys/archive/refs/tags/sequential/v%{ver_sequential}.tar.gz#/%{_name}-sequential-%{ver_sequential}.tar.gz
#!RemoteAsset:  sha256:1b285fbc3ac64256bb59116a290376ee9010d2f23338621b9d0f096f8d1cd883
Source2:        https://github.com/moby/sys/archive/refs/tags/mountinfo/v%{ver_mountinfo}.tar.gz#/%{_name}-mountinfo-%{ver_mountinfo}.tar.gz
#!RemoteAsset:  sha256:cfa55aa185b1f9c44bee3d348caf79cf72d654f2a1c8e9c5a96e47da7905309e
Source3:        https://github.com/moby/sys/archive/refs/tags/signal/v%{ver_signal}.tar.gz#/%{_name}-signal-%{ver_signal}.tar.gz
#!RemoteAsset:  sha256:c8ea64c2a9ec1f2ddc338c22818ad7a39d1092e62a36df3950b359dbfd96d49b
Source4:        https://github.com/moby/sys/archive/refs/tags/user/v%{ver_user}.tar.gz#/%{_name}-user-%{ver_user}.tar.gz
#!RemoteAsset:  sha256:9caafb9a772df5fe3b9d9fad0102c24ffac5ad0ef04fb9b5077c372bcafab4ae
Source5:        https://github.com/moby/sys/archive/refs/tags/userns/v%{ver_userns}.tar.gz#/%{_name}-userns-%{ver_userns}.tar.gz

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/moby/sys/atomicwriter) = %{ver_atomicwriter}
Provides:       go(github.com/moby/sys/mountinfo) = %{ver_mountinfo}
Provides:       go(github.com/moby/sys/sequential) = %{ver_sequential}
Provides:       go(github.com/moby/sys/signal) = %{ver_signal}
Provides:       go(github.com/moby/sys/user) = %{ver_user}
Provides:       go(github.com/moby/sys/userns) = %{ver_userns}

Requires:       go(golang.org/x/sys)

%description
This package bundles the independently tagged atomicwriter, sequential,
mountinfo, signal, user, and userns modules from github.com/moby/sys.

%prep
%setup -q -c -T -a 0
%setup -q -D -T -a 1
%setup -q -D -T -a 2
%setup -q -D -T -a 3
%setup -q -D -T -a 4
%setup -q -D -T -a 5

%install
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}
install -m 0644 %{dir_atomicwriter}/LICENSE \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/LICENSE

for module in atomicwriter sequential mountinfo signal user userns; do
    install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/${module}
done
cp -a %{dir_atomicwriter}/atomicwriter/. \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/atomicwriter/
cp -a %{dir_sequential}/sequential/. \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/sequential/
cp -a %{dir_mountinfo}/mountinfo/. \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/mountinfo/
cp -a %{dir_signal}/signal/. \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/signal/
cp -a %{dir_user}/user/. \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/user/
cp -a %{dir_userns}/userns/. \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/userns/

%check
%go_common
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf %{_builddir}/go/src/%{go_import_path}
install -d %{_builddir}/go/src/%{go_import_path}
for module in atomicwriter sequential mountinfo signal user userns; do
    cp -a %{buildroot}%{go_sys_gopath}/%{go_import_path}/${module} \
        %{_builddir}/go/src/%{go_import_path}/${module}
done

for module in atomicwriter sequential mountinfo signal user userns; do
    pushd %{_builddir}/go/src/%{go_import_path}/${module}
    # Compile every package and its tests before tolerating sandbox-only failures.
    go test -vet=off -run '^$' ./...
    if [ "${module}" = mountinfo ]; then
        # Mount tests may lack CAP_SYS_ADMIN in the OBS worker.
        go test -vet=off ./... || :
    else
        go test -vet=off ./...
    fi
    popd
done

%files
%license %{go_sys_gopath}/%{go_import_path}/LICENSE
%{go_sys_gopath}/%{go_import_path}/atomicwriter
%{go_sys_gopath}/%{go_import_path}/mountinfo
%{go_sys_gopath}/%{go_import_path}/sequential
%{go_sys_gopath}/%{go_import_path}/signal
%{go_sys_gopath}/%{go_import_path}/user
%{go_sys_gopath}/%{go_import_path}/userns

%changelog
%autochangelog
