# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           webrtc
%define go_import_path  github.com/pion/webrtc/v3
%define go_test_exclude %{go_import_path}

Name:           go-github-pion-webrtc-v3
Version:        3.3.6
Release:        %autorelease
Summary:        A pure Go implementation of the WebRTC API
License:        MIT AND BSD-3-Clause
URL:            https://github.com/pion/webrtc
#!RemoteAsset:  sha256:eb4fc91eaae0737a4c331a12c193cd12032cdf39d9e3d42a3e352a0fedb9e00f
Source0:        https://github.com/pion/webrtc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch0:         0001-copy-RTP-padding-size-to-header.patch

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/datachannel)
BuildRequires:  go(github.com/pion/dtls/v2)
BuildRequires:  go(github.com/pion/ice/v2)
BuildRequires:  go(github.com/pion/interceptor)
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/randutil)
BuildRequires:  go(github.com/pion/rtcp)
BuildRequires:  go(github.com/pion/rtp)
BuildRequires:  go(github.com/pion/sctp)
BuildRequires:  go(github.com/pion/sdp/v3)
BuildRequires:  go(github.com/pion/srtp/v2)
BuildRequires:  go(github.com/pion/stun)
BuildRequires:  go(github.com/pion/transport/v2)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/pion/webrtc/v3) = %{version}

Requires:       go(github.com/pion/datachannel)
Requires:       go(github.com/pion/dtls/v2)
Requires:       go(github.com/pion/ice/v2)
Requires:       go(github.com/pion/interceptor)
Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/randutil)
Requires:       go(github.com/pion/rtcp)
Requires:       go(github.com/pion/rtp)
Requires:       go(github.com/pion/sctp)
Requires:       go(github.com/pion/sdp/v3)
Requires:       go(github.com/pion/srtp/v2)
Requires:       go(github.com/pion/stun)
Requires:       go(github.com/pion/transport/v2)
Requires:       go(golang.org/x/net)

%description
A pure Go implementation of the WebRTC API

%files
%doc README.md
%license LICENSE test-wasm/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
