# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-test-runner
Version:        0.1.3
Release:        %autorelease
Summary:        Unified runner for installed package tests
License:        MulanPSL-2.0
URL:            https://github.com/openRuyi-Project/openRuyi
Source0:        openruyi-test
Source1:        LICENSE
Source2:        test_openruyi_test.py
Source3:        README.md
BuildArch:      noarch

BuildRequires:  python3
Requires:       python3
Requires:       rpm

%description
Discovers installed package tests, enforces per-test timeouts, saves logs and
writes a machine-readable result summary. It supports freedesktop installed
test descriptors and versioned openRuyi test manifests.

%install
install -Dpm0755 %{SOURCE0} %{buildroot}%{_bindir}/openruyi-test
ln -s openruyi-test %{buildroot}%{_bindir}/pkg-test
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dpm0644 %{SOURCE3} %{buildroot}%{_docdir}/%{name}/README.md
install -d %{buildroot}%{_datadir}/openruyi-tests/v1
install -d %{buildroot}%{_libexecdir}/openruyi-tests

%check
python3 %{SOURCE2}

%files
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%{_bindir}/openruyi-test
%{_bindir}/pkg-test
%dir %{_datadir}/openruyi-tests
%dir %{_datadir}/openruyi-tests/v1
%dir %{_libexecdir}/openruyi-tests

%changelog
%autochangelog
