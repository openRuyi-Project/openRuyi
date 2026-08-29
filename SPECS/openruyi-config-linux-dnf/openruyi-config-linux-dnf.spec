# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-config-linux-dnf
Version:        20260602
Release:        %autorelease
Summary:        Specific DNF5 configuration files for Linux kernel
License:        GPL-2.0-or-later
URL:            https://github.com/openRuyi-Project/openRuyi
BuildArch:      noarch

# libdnf5 owns the directories we need
Requires:       libdnf5
Supplements:    libdnf5

%sourcelist
linux-policy.conf

%description
This package contains the DNF configuration for the openRuyi Linux
kernel maintainence.

%prep
%setup -c -T
cp -p %{sources} .

%install
install -p -Dm 644 -t %{buildroot}%{_datadir}/dnf5/libdnf.conf.d linux-policy.conf

%files
%{_datadir}/dnf5/libdnf.conf.d/linux-policy.conf

%changelog
%autochangelog
