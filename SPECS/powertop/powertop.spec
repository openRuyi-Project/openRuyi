# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           powertop
Version:        2.15
Release:        %autorelease
Summary:        Power consumption monitor
License:        GPL-2.0-only
URL:            https://github.com/fenrus75/powertop
#!RemoteAsset
Source0:        https://github.com/fenrus75/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        powertop.service
Patch1:         powertop-2.7-always-create-params.patch

BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  systemd
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  bash-completion

Requires(post): coreutils
%{?systemd_requires}


%description
PowerTOP is a Linux* tool used to diagnose issues with power consumption and
power management. In addition to being a diagnostic tool, PowerTOP also has
an interactive mode you can use to experiment with various power management
settings, for cases where the Linux distribution has not enabled those settings.

%conf -p
# https://www.gnu.org/software/gettext/manual/html_node/autopoint-Invocation.html
sed -i -e 's|AM_GNU_GETTEXT_VERSION|AM_GNU_GETTEXT_REQUIRE_VERSION|' configure.ac
# workaroud for 'error: too many loops'
autoreconf -fi || autoreconf -fi

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
%license COPYING
%doc README.md README.traceevent CONTRIBUTE.md TODO
%{_sbindir}/powertop
%{_unitdir}/powertop.service
%dir %{_localstatedir}/cache/powertop
%ghost %{_localstatedir}/cache/powertop/saved_parameters.powertop
%ghost %{_localstatedir}/cache/powertop/saved_results.powertop
%{_datadir}/bash-completion/completions/powertop
%{_mandir}/man8/powertop.8*

%changelog
%autochangelog
