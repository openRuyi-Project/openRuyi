# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           meson
Version:        1.10.2
Release:        %autorelease
Summary:        High productivity build system
License:        Apache-2.0
URL:            https://mesonbuild.com/
VCS:            git:https://github.com/mesonbuild/meson.git
#!RemoteAsset:  sha256:7890287d911dd4ee1ebd0efb61ed0321bfcd87c725df923a837cf90c6508f96b
Source0:        https://github.com/mesonbuild/meson/releases/download/%{version}/meson-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  expat

Requires:       python3dist(setuptools)
Requires:       ninja
Requires:       python3

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%prep
%autosetup -p1 -n meson-%{version}
# Macro should not change when we are redefining bindir
sed -i -e "/^%%__meson /s| .*$| %{_bindir}/%{name}|" data/macros.meson

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir} data/macros.meson
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions/ data/shell-completions/bash/meson
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions/ data/shell-completions/zsh/_meson

%files
%license COPYING
%{_bindir}/meson
%{python3_sitelib}/mesonbuild/
%{python3_sitelib}/meson-*.dist-info/
%{_mandir}/man1/meson.1*
%{_rpmmacrodir}/macros.meson
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
%{_datadir}/bash-completion/completions/meson
%{_datadir}/zsh/site-functions/_meson

%changelog
%{?autochangelog}
