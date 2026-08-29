# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit c43123398cb8e0941c94fbee1f3dec8f6514e1bf
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mkosi
Version:        25.3+git20251224.%{shortcommit}
Release:        %autorelease
Summary:        Create bespoke OS images
License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/mkosi
#!RemoteAsset:  sha256:5a1fb73305fe6c531e72b72deee906b1870bd3d197a5f7f1569a8bba4949b878
Source:         https://github.com/systemd/mkosi/archive/%{commit}/mkosi-%{commit}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildSystem:    pyproject
Patch0:         0001-Add-openruyi-support.patch

BuildOption(prep):  -n %{name}-%{commit}
BuildOption(install):  %{name} +auto

Requires:       python3
Requires:       coreutils
Requires:       util-linux
Requires:       mtools
Requires:       libseccomp
Requires:       dosfstools
Requires:       systemd-repart
Requires:       system-release

%description
A fancy wrapper around package managers that generates disk images with a
number of bells and whistles for containers, VMs, initrds, and extensions.
See https://mkosi.systemd.io/ for documentation.

%package       initrd
Summary:       Build initrds locally using mkosi
Requires:      %{name} = %{version}
Requires:      (dnf5 or dnf)

%description   initrd
This package provides the CLI and the plugin for kernel-install to build
initrds with mkosi locally.

%package       addon
Summary:       Build PE addons locally using mkosi
Requires:      %{name} = %{version}
Requires:      systemd-boot
%description   addon
This package provides the CLI and the plugin for kernel-install to build
PE addons for distribution-signed unified kernel images with mkosi locally.

%generate_buildrequires
%pyproject_buildrequires

%build -a
bin/mkosi completion bash > mkosi.bash
bin/mkosi completion fish > mkosi.fish
bin/mkosi completion zsh > mkosi.zsh

%install -a
install -d -m 755 %{buildroot}%{_prefix}/lib/kernel/install.d/
install -m 0755 kernel-install/50-mkosi.install %{buildroot}%{_prefix}/lib/kernel/install.d/
install -m 0755 kernel-install/51-mkosi-addon.install %{buildroot}%{_prefix}/lib/kernel/install.d/
mkdir -p %{buildroot}%{_prefix}/lib/mkosi-initrd
mkdir -p %{buildroot}%{_sysconfdir}/mkosi-initrd
mkdir -p %{buildroot}%{_prefix}/lib/mkosi-addon
mkdir -p %{buildroot}%{_sysconfdir}/mkosi-addon

install -m 0644 -D mkosi.bash %{buildroot}%{_datadir}/bash-completion/completions/mkosi
install -m 0644 -D mkosi.fish %{buildroot}%{_datadir}/fish/completions/mkosi.fish
install -m 0644 -D mkosi.zsh %{buildroot}%{_datadir}/zsh/site-functions/_mkosi


%files -f %{pyproject_files}
%license LICENSES/*
%doc README.md
%{_bindir}/mkosi*
%{_datadir}/bash-completion/completions/mkosi
%{_datadir}/fish/completions/mkosi.fish
%{_datadir}/zsh/site-functions/_mkosi

%files initrd
%{_bindir}/mkosi-initrd
%{_prefix}/lib/kernel/install.d/50-mkosi.install
%ghost %dir %{_prefix}/lib/mkosi-initrd
%ghost %dir %{_sysconfdir}/mkosi-initrd

%files addon
%{_bindir}/mkosi-addon
%{_prefix}/lib/kernel/install.d/51-mkosi-addon.install
%ghost %dir %{_prefix}/lib/mkosi-addon
%ghost %dir %{_sysconfdir}/mkosi-addon

%changelog
%autochangelog
