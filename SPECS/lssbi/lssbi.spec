# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zhouqi Jiang <jiangzhouqi25@mails.ucas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lssbi
Version:        0.0.1
Release:        %autorelease
Summary:        List information about the active RISC-V SBI environment
License:        MIT OR MulanPSL-2.0
URL:            https://github.com/rustsbi/lssbi
VCS:            git:https://github.com/rustsbi/lssbi.git
#!RemoteAsset:  sha256:b3cdf66c215d21c80f98eb0458f2f4937c4add7278776131f571d356feae04b0
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  riscv64
BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  rust >= 1.85
BuildRequires:  cargo
BuildRequires:  gettext-devel
BuildRequires:  crate(clap-4) >= 4.5.0
BuildRequires:  crate(clap-4/cargo) >= 4.5.0
BuildRequires:  crate(clap-4/derive) >= 4.5.0
BuildRequires:  crate(clap-4/help) >= 4.5.0
BuildRequires:  crate(clap-4/std) >= 4.5.0
BuildRequires:  crate(clap-4/usage) >= 4.5.0
BuildRequires:  crate(gettext-rs-0.8/default) >= 0.8.0
BuildRequires:  crate(gettext-rs-0.8/gettext-system) >= 0.8.0
BuildRequires:  crate(jep106-0.3) >= 0.3.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(polib-0.3/default) >= 0.3.0
BuildRequires:  crate(sbi-spec-0.0.9/default) >= 0.0.9
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(unicode-width-0.2/default) >= 0.2.0

Recommends:     %{name}-dkms = %{version}-%{release}

%description
lssbi is an unprivileged command-line tool that reports the active RISC-V SBI
specification, implementation, supported extensions, firmware features,
machine identifiers, and known firmware vulnerabilities.

%package        dkms
Summary:        DKMS backend for lssbi
License:        GPL-2.0-only
BuildArch:      noarch

Requires:       dkms >= 2.2.0.3
Requires:       gcc
Requires:       make
Requires:       linux-devel

AutoReqProv:    no

%description    dkms
This package contains the lssbi_probe kernel module source and DKMS
configuration used by lssbi to inspect the active RISC-V SBI environment.

%prep -a
# Resolve against the crate versions provided by the openRuyi registry.
rm -f Cargo.lock

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} PROFILE=release ./install.sh

install -d %{buildroot}%{_usrsrc}/%{name}-%{version}/kernel
install -pm 0644 dkms.conf %{buildroot}%{_usrsrc}/%{name}-%{version}/
install -pm 0644 kernel/Kbuild kernel/lssbi_probe.c \
    %{buildroot}%{_usrsrc}/%{name}-%{version}/kernel/
install -Dpm 0644 modules-load.d/lssbi.conf \
    %{buildroot}%{_modulesloaddir}/lssbi.conf

%find_lang %{name} --generate-subpackages

%post dkms
dkms add -m %{name} -v %{version} --rpm_safe_upgrade ||:
dkms install -m %{name} -v %{version} ||:

%preun dkms
if [ "$1" = "0" ]; then
    dkms remove -m %{name} -v %{version} --all --rpm_safe_upgrade ||:
fi

%files
%doc CHANGELOG.md README.md
%license LICENSE-MIT LICENSE-MULAN
%{_bindir}/lssbi

%files dkms
%license LICENSE-GPL-2.0
%{_usrsrc}/%{name}-%{version}/
%{_modulesloaddir}/lssbi.conf

%changelog
%autochangelog
