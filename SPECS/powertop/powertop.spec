# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           powertop
Version:        2.16.1
Release:        %autorelease
Summary:        Power consumption monitor
License:        GPL-2.0-only
URL:            https://github.com/fenrus75/powertop
#!RemoteAsset:  sha256:73d5e96d992ed7f040e17c6c9130deebcf42c38990711840981c7afac6f7832f
Source0:        https://github.com/fenrus75/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        powertop.service
BuildSystem:    meson

BuildOption(conf):  -Dnls=true

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libtracefs)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  bash-completion
BuildRequires:  systemd-rpm-macros

Requires(post): coreutils
%{?systemd_requires}


%description
PowerTOP is a Linux* tool used to diagnose issues with power consumption and
power management. In addition to being a diagnostic tool, PowerTOP also has
an interactive mode you can use to experiment with various power management
settings, for cases where the Linux distribution has not enabled those settings.

%install -a
# Prepares cache files to ensure persistence of saved parameters and results upon first run
install -Dd %{buildroot}%{_localstatedir}/cache/%{name}
touch %{buildroot}%{_localstatedir}/cache/%{name}/{saved_parameters.powertop,saved_results.powertop}

%find_lang %{name} --generate-subpackages

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/powertop.service

%preun
%systemd_preun powertop.service

%postun
%systemd_postun_with_restart powertop.service

%post
%systemd_post powertop.service
# Hack for powertop not to show warnings on first start
touch %{_localstatedir}/cache/powertop/{saved_parameters.powertop,saved_results.powertop} &> /dev/null || :

%files -f %{name}.lang
%doc README.md CONTRIBUTE.md TODO
%license COPYING
%{_bindir}/powertop
%{_unitdir}/powertop.service
%dir %{_localstatedir}/cache/powertop
%ghost %{_localstatedir}/cache/powertop/saved_parameters.powertop
%ghost %{_localstatedir}/cache/powertop/saved_results.powertop
%{_datadir}/bash-completion/completions/powertop
%{_mandir}/man8/powertop.8*

%changelog
%autochangelog
