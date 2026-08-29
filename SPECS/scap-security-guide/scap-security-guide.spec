# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           scap-security-guide
Version:        0.1.80
Release:        %autorelease
Summary:        Security guidance and baselines in SCAP formats
License:        BSD-3-Clause
URL:            https://github.com/ComplianceAsCode/content
#!RemoteAsset:  sha256:3e056f460d6626b7109202cb94b2f7dd6af6ff89db22b699fede65ba9316919f
Source:         https://github.com/ComplianceAsCode/content/releases/download/v%{version}/scap-security-guide-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    cmake

Patch2000:      2000-add-support-for-openRuyi.patch

BuildOption(conf):  -DSSG_SCE_ENABLED=ON

BuildRequires:  cmake
BuildRequires:  libxslt
BuildRequires:  openscap
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(setuptools)

Requires:       xml-common
Requires:       openscap

%description
The scap-security-guide project provides a guide for configuration of the
system from the final system's security point of view. The guidance is specified
in the Security Content Automation Protocol (SCAP) format and constitutes
a catalog of practical hardening advice, linked to government requirements
where applicable. The project bridges the gap between generalized policy
requirements and specific implementation guidelines. The system
administrator can use the oscap CLI tool from openscap-scanner package, or the
scap-workbench GUI tool from scap-workbench package to verify that the system
conforms to provided guideline. Refer to scap-security-guide(8) manual page for
further information.

# No tests
%check

%files
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/Contributors.md
%doc %{_docdir}/%{name}/guides/*.html
%doc %{_docdir}/%{name}/tables/*.html
%{_datadir}/xml/scap/ssg/content
%{_datadir}/%{name}/kickstart
%{_datadir}/%{name}/ansible
%{_datadir}/%{name}/tailoring
%{_datadir}/%{name}/bash
%{_mandir}/man8/scap-security-guide.8.*

%changelog
%autochangelog
