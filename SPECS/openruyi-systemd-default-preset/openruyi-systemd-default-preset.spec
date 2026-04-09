# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-systemd-default-preset
Version:        20260316
Release:        %{autorelease}
Summary:        Default systemd preset configuration for openRuyi
License:        MulanPSL-2.0
BuildArch:      noarch

Source0:        90-openruyi-default.preset
Source1:        80-openruyi-server.preset
Source2:        80-openruyi-workstation.preset
Source3:        80-openruyi-desktop.preset

Requires:       systemd

%description
This package provides the default systemd preset policy for openRuyi.
Systemd presets explicitly define which services should be enabled or
disabled by default upon package installation.

%package        server
Summary:        Server specific systemd presets for openRuyi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    server
Overrides the base presets to enable common services for the Server edition.

%package        workstation
Summary:        Workstation specific systemd presets for openRuyi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    workstation
Overrides the base presets to enable common services for the Workstation edition.

%package        desktop
Summary:        Desktop specific systemd presets for openRuyi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    desktop
Overrides the base presets to enable common services for the Desktop edition.

%prep
# Nothing to prep

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_presetdir}

install -m 0644 %{SOURCE0} %{buildroot}%{_presetdir}/90-openruyi-default.preset
install -m 0644 %{SOURCE1} %{buildroot}%{_presetdir}/80-openruyi-server.preset
install -m 0644 %{SOURCE2} %{buildroot}%{_presetdir}/80-openruyi-workstation.preset
install -m 0644 %{SOURCE3} %{buildroot}%{_presetdir}/80-openruyi-desktop.preset

%files
%{_presetdir}/90-openruyi-default.preset

%files server
%{_presetdir}/80-openruyi-server.preset

%files workstation
%{_presetdir}/80-openruyi-workstation.preset

%files desktop
%{_presetdir}/80-openruyi-desktop.preset

%changelog
%autochangelog
