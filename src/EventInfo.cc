#include "../interface/EventInfo.hh"
#include "boost/format.hpp"

namespace ic {
EventInfo::EventInfo()
    : is_data_(false),
      event_(0),
      run_(0),
      lumi_block_(0),
      bunch_crossing_(0),
      jet_rho_(0.),
      lepton_rho_(0.),
      gen_ht_(0.),
      n_outgoing_partons_(0),
      npNLO_(-1),
      gen_mll_(0.),
      good_vertices_(0),
      pt_h_(0.),
      n_jets30_(0), 
      stage1_cat_(0) {}

EventInfo::~EventInfo() {}

void EventInfo::Print() const {
  std::cout << boost::format("%s\n") % std::string(30, '=');
  std::cout << boost::format("%-17s | %10i\n")   % "event"          % event_;
  std::cout << boost::format("%-17s | %10i\n")   % "lumi_block"     % lumi_block_;
  std::cout << boost::format("%-17s | %10i\n")   % "run"            % run_;
  std::cout << boost::format("%-17s | %10.3f\n") % "jet_rho"        % jet_rho_;
  std::cout << boost::format("%-17s | %10.3f\n") % "lepton_rho"     % lepton_rho_;
  std::cout << boost::format("%-17s | %10i\n")   % "good_vertices"  % good_vertices_;
  std::cout << boost::format("%-17s | %10i\n")   % "n_jets30"       % n_jets30_;
  std::cout << boost::format("%-17s | %10.3f\n") % "pt_h"           % pt_h_;
  std::cout << boost::format("%s\n")      % std::string(30, '-');
  std::cout << boost::format("%-17s\n")   % "weights";
  std::cout << boost::format("%s\n")      % std::string(30, '-');
  SDMap::const_iterator it = weights_.begin();
  SBMap::const_iterator its = weight_status_.begin();
  for (; it != weights_.end() && its != weight_status_.end(); ++it, ++its) {
    std::cout << boost::format("%-17s | %6.3f %3i\n") % it->first % it->second %
                     its->second;
  }
  if (filters_.size() > 0) {
    std::cout << boost::format("%s\n") % std::string(30, '-');
    std::cout << boost::format("%-17s\n")   % "filters";
    std::cout << boost::format("%s\n")      % std::string(30, '-');
    TBMap::const_iterator itf = filters_.begin();
    for (; itf != filters_.end(); ++itf) {
      std::cout << boost::format("%-21s | %6.3f\n") % itf->first % itf->second;
    }
  }
  std::cout << boost::format("%s\n")      % std::string(30, '=');
}
}
