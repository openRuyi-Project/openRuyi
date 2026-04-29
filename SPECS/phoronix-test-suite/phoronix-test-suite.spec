# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global date 20260415
%global commit 4e8c4ffe2a133ccfda9dd104c08575ee5fcbc68b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           phoronix-test-suite
Version:        10.8.4+git%{date}.%{shortcommit}
Release:        %autorelease
Summary:        An Automated, Open-Source Testing Framework
License:        GPL-3.0-or-later
URL:            http://www.phoronix-test-suite.com/
VCS:            git:https://github.com/phoronix-test-suite/phoronix-test-suite
#!RemoteAsset:  sha256:8ae52008757503a57406f546dd4b49b497a929748659e04757b44f1d436a5d1f
Source0:        https://github.com/phoronix-test-suite/phoronix-test-suite/archive/%{commit}/phoronix-test-suite-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  systemd-rpm-macros

Requires:       php-cli
Requires:       php-xml
Requires:       php-json
Requires:       php-openssl
Requires:       php-gd
Requires:       php-sqlite3
Requires:       php-posix
Requires:       php-curl
Requires:       hicolor-icon-theme
%{?systemd_requires}

%description
The Phoronix Test Suite is the most comprehensive testing and benchmarking
platform available for the Linux operating system. This software is designed to
effectively carry out both qualitative and quantitative benchmarks.

%prep
%autosetup -p1 -n %{name}-%{commit}

%install
export DESTDIR=%{buildroot}
./install-sh %{_prefix}

%post
%systemd_post phoromatic-client.service phoromatic-server.service phoronix-result-server.service

%preun
%systemd_preun phoromatic-client.service phoromatic-server.service phoronix-result-server.service

%postun
%systemd_postun_with_restart phoromatic-client.service phoromatic-server.service phoronix-result-server.service

%files
%{_bindir}/phoronix-test-suite
%doc documentation/*
%doc AUTHORS ChangeLog COPYING
%{_datadir}/phoronix-test-suite/
%{_datadir}/icons/hicolor/48x48/apps/phoronix-test-suite.png
%{_datadir}/icons/hicolor/64x64/mimetypes/application-x-openbenchmarking.png
%{_mandir}/man1/phoronix-test-suite.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/metainfo/com.phoronix_test_suite.phoronix_test_suite.metainfo.xml
%{_unitdir}/*.service

%changelog
%autochangelog
