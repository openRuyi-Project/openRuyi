# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bash-completion
Version:        2.17.0
Release:        %autorelease
Summary:        Programmable completion for Bash
License:        GPL-2.0-or-later
URL:            https://github.com/scop/bash-completion
#!RemoteAsset:  sha256:dd9d825e496435fb3beba3ae7bea9f77e821e894667d07431d1d4c8c570b9e58
Source0:        https://github.com/scop/bash-completion/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        macros.bash-completion
BuildArch:      noarch
BuildSystem:    autotools

BuildRequires:  automake
BuildRequires:  make

Requires:       bash

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%install -a
# Install macros
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.bash-completion

%files
%license COPYING
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md README.md
%doc doc/configuration.md doc/styleguide.md
%config(noreplace) %{_sysconfdir}/profile.d/bash_completion.sh
%{_sysconfdir}/bash_completion.d/000_bash_completion_compat.bash
%{_datadir}/bash-completion/
%{_rpmconfigdir}/macros.d/macros.bash-completion

%files devel
%{_datadir}/cmake/
%{_datadir}/pkgconfig/bash-completion.pc

%changelog
%autochangelog
