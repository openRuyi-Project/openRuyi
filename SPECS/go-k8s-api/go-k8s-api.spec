# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  k8s.io/api

Name:           go-k8s-api
Version:        0.36.1
Release:        %autorelease
Summary:        Schema of the external API types that are served by the Kubernetes API server
License:        Apache-2.0
URL:            https://github.com/kubernetes/api
#!RemoteAsset:  sha256:f7a599f2cc76591c6575476102e2c65c83edb733bfe6a6829649b4f67312eb91
Source0:        https://github.com/kubernetes/api/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(k8s.io/apimachinery/pkg/api/apitesting/fuzzer)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/operation)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/safe)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/validate)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/validate/content)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/fuzzer)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  go(k8s.io/apimachinery/pkg/types)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/validation/field)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/klog/v2/ktesting)

Provides:       go(k8s.io/api) = %{version}
Provides:       go(k8s.io/api/admission/v1) = %{version}
Provides:       go(k8s.io/api/admission/v1beta1) = %{version}
Provides:       go(k8s.io/api/admissionregistration/v1) = %{version}
Provides:       go(k8s.io/api/admissionregistration/v1alpha1) = %{version}
Provides:       go(k8s.io/api/admissionregistration/v1beta1) = %{version}
Provides:       go(k8s.io/api/apidiscovery/v2) = %{version}
Provides:       go(k8s.io/api/apidiscovery/v2beta1) = %{version}
Provides:       go(k8s.io/api/apiserverinternal/v1alpha1) = %{version}
Provides:       go(k8s.io/api/apps/v1) = %{version}
Provides:       go(k8s.io/api/apps/v1beta1) = %{version}
Provides:       go(k8s.io/api/apps/v1beta2) = %{version}
Provides:       go(k8s.io/api/authentication/v1) = %{version}
Provides:       go(k8s.io/api/authentication/v1alpha1) = %{version}
Provides:       go(k8s.io/api/authentication/v1beta1) = %{version}
Provides:       go(k8s.io/api/authorization/v1) = %{version}
Provides:       go(k8s.io/api/authorization/v1beta1) = %{version}
Provides:       go(k8s.io/api/autoscaling/v1) = %{version}
Provides:       go(k8s.io/api/autoscaling/v2) = %{version}
Provides:       go(k8s.io/api/batch/v1) = %{version}
Provides:       go(k8s.io/api/batch/v1beta1) = %{version}
Provides:       go(k8s.io/api/certificates/v1) = %{version}
Provides:       go(k8s.io/api/certificates/v1alpha1) = %{version}
Provides:       go(k8s.io/api/certificates/v1beta1) = %{version}
Provides:       go(k8s.io/api/coordination/v1) = %{version}
Provides:       go(k8s.io/api/coordination/v1alpha2) = %{version}
Provides:       go(k8s.io/api/coordination/v1beta1) = %{version}
Provides:       go(k8s.io/api/core/v1) = %{version}
Provides:       go(k8s.io/api/discovery/v1) = %{version}
Provides:       go(k8s.io/api/discovery/v1beta1) = %{version}
Provides:       go(k8s.io/api/events/v1) = %{version}
Provides:       go(k8s.io/api/events/v1beta1) = %{version}
Provides:       go(k8s.io/api/extensions/v1beta1) = %{version}
Provides:       go(k8s.io/api/flowcontrol/v1) = %{version}
Provides:       go(k8s.io/api/flowcontrol/v1beta1) = %{version}
Provides:       go(k8s.io/api/flowcontrol/v1beta2) = %{version}
Provides:       go(k8s.io/api/flowcontrol/v1beta3) = %{version}
Provides:       go(k8s.io/api/imagepolicy/v1alpha1) = %{version}
Provides:       go(k8s.io/api/networking/v1) = %{version}
Provides:       go(k8s.io/api/networking/v1beta1) = %{version}
Provides:       go(k8s.io/api/node/v1) = %{version}
Provides:       go(k8s.io/api/node/v1alpha1) = %{version}
Provides:       go(k8s.io/api/node/v1beta1) = %{version}
Provides:       go(k8s.io/api/policy/v1) = %{version}
Provides:       go(k8s.io/api/policy/v1beta1) = %{version}
Provides:       go(k8s.io/api/rbac/v1) = %{version}
Provides:       go(k8s.io/api/rbac/v1alpha1) = %{version}
Provides:       go(k8s.io/api/rbac/v1beta1) = %{version}
Provides:       go(k8s.io/api/resource/v1) = %{version}
Provides:       go(k8s.io/api/resource/v1alpha3) = %{version}
Provides:       go(k8s.io/api/resource/v1beta1) = %{version}
Provides:       go(k8s.io/api/resource/v1beta2) = %{version}
Provides:       go(k8s.io/api/scheduling/v1) = %{version}
Provides:       go(k8s.io/api/scheduling/v1alpha2) = %{version}
Provides:       go(k8s.io/api/scheduling/v1beta1) = %{version}
Provides:       go(k8s.io/api/storage/v1) = %{version}
Provides:       go(k8s.io/api/storage/v1alpha1) = %{version}
Provides:       go(k8s.io/api/storage/v1beta1) = %{version}
Provides:       go(k8s.io/api/storagemigration/v1beta1) = %{version}

Requires:       go(k8s.io/apimachinery/pkg/api/equality)
Requires:       go(k8s.io/apimachinery/pkg/api/operation)
Requires:       go(k8s.io/apimachinery/pkg/api/resource)
Requires:       go(k8s.io/apimachinery/pkg/api/safe)
Requires:       go(k8s.io/apimachinery/pkg/api/validate)
Requires:       go(k8s.io/apimachinery/pkg/api/validate/content)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1)
Requires:       go(k8s.io/apimachinery/pkg/runtime)
Requires:       go(k8s.io/apimachinery/pkg/runtime/schema)
Requires:       go(k8s.io/apimachinery/pkg/types)
Requires:       go(k8s.io/apimachinery/pkg/util/intstr)
Requires:       go(k8s.io/apimachinery/pkg/util/validation)
Requires:       go(k8s.io/apimachinery/pkg/util/validation/field)
Requires:       go(k8s.io/klog/v2)


%description
The Kubernetes API module contains the external API type definitions served by
the Kubernetes API server. It provides group/version import paths such as
apps/v1, batch/v1, core/v1, discovery/v1, and networking/v1 for Go clients and
controllers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
